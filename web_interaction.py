from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import wanikani_api.client
import time
import pandas as pd
import re
import os


class Bunpro:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.imported_vocab_list = []
        self.mastered_vocab = []
        self.start_time = time.time()


    def login(self):
        """Opens Selenium on Bunpro and logs User in with the Account Data from the environment Variables"""
        self.driver.get("https://bunpro.jp/login")
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, value="input#user_email").click()
        self.driver.find_element(By.CSS_SELECTOR, value="input#user_email").send_keys(os.getenv("BUNPRO_EMAIL"))
        pass_field = self.driver.find_element(By.ID, value="user_password")
        pass_field.send_keys(os.getenv("BUNPRO_PASSWORD"))
        pass_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def get_vocab(self):
        """Add all the known Vocabulary listed in the wanikani_vocab.csv from Wanikani and anki_vocab.txt from Anki ot the imported_vocab_list"""
        # Wanikani Vocab
        self.imported_vocab_list = pd.read_csv("files/wanikani_vocab.csv")["Vocab"].to_list()

        # Anki Vocab
        with open("files/anki_vocab.txt", encoding='utf-8') as file:
            content = file.readlines()

        words = [re.sub("[\(\[\{].*?[\)\]\}]", "", word.replace('"', "").strip()) for word in content]
        for word in words:
            word = word.replace("\ufeff", "").split(" ")
            for entry in word:
                self.imported_vocab_list.append(entry)


    def set_learnt(self, item):
        time.sleep(0.3)
        item.find_element(By.CLASS_NAME, value="dropdown-toggle").click() # click on dropdown
        time.sleep(0.3)
        buttons = item.find_elements(By.CSS_SELECTOR, value="div.dropdown-menu li.u-flex")
        for button in buttons:
            if button.text == "Mark as Mastered":
                button.click()


    def edit_deck(self, page, stop_page, deck):
        self.driver.get(f"https://bunpro.jp/decks/{deck}?page={str(page)}")
        page_start_time = time.time() # Starts timer for Page
        time.sleep(5)

        if stop_page == 0: # find last page of a deck
            stop_page = int(self.driver.find_elements(By.CSS_SELECTOR, value="nav.pagy-nav span.page")[-2].text)
            print(stop_page)
            time.sleep(5)

        items = self.driver.find_elements(By.CLASS_NAME, value="deck-info-card") # Each word
        for item in items: # For each Word
            srs_stage = item.find_elements(By.CSS_SELECTOR, value="div.u-flex.u-items_center")[-1].text # find the SRS Stage of the Word
            vocab = item.find_element(By.CLASS_NAME, value="deck-card-title").text.split("\n") # Find Word name
            if len(vocab) <= 2: # if there are less than two entries than the word has no Kanji between Kana
                vocab = vocab[0]
            else: # Skip the Kanji
                vocab = f"{vocab[0]}{vocab[-1]}"
            print(f"working on {vocab} with SRS: {srs_stage}")

            if vocab in self.imported_vocab_list and srs_stage != "SRS 12":
                print(f"{vocab}should be mastered")
                self.set_learnt(item) # set word as mastered
                self.mastered_vocab.append(vocab) # add word to mastered list
            elif srs_stage == "SRS12":
                print(f"{vocab} already mastered")
            else:
                print(f"{vocab} not known")

        print(f"Page {page} took {time.time() - page_start_time} seconds")
        print(f"Program has been running for {time.time() - self.start_time} seconds")
        time.sleep(2)
        if page < stop_page: # if the last page was not reached, go to the next
            self.edit_deck(page + 1, stop_page, deck)

    def print_word_list(self):
        print(
            f"{self.imported_vocab_list}\nThese are the words, that will be set to known.\nThey are {len(self.imported_vocab_list)} words")

class Wanikani:
    def __init__(self):
        self.df = pd.DataFrame()
        self.client = wanikani_api.client.Client(os.getenv("WANIKANI_API"))
        self.words = []
        self.mean = []

    def create_list(self):
        all_vocabulary = self.client.subjects(types="vocabulary", fetch_all=True)
        for word in all_vocabulary:
            self.words.append(word.characters)
        for meaning in all_vocabulary:
            self.mean.append(meaning.meanings[0].meaning)
        self.df["Vocab"] = self.words
        self.df["Meaning"] = self.mean
        self.df.to_csv("files/wanikani_vocab.csv", index=False)


