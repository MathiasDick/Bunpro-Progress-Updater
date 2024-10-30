from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re
import os

# SETUP -------------------------------------------------------------------------------------#

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

imported_vocab_list = []
mastered_vocab = []

# ----------------------------------------------------------------------------------------------#


def login():
    driver.get("https://bunpro.jp/login")
    time.sleep(5)
    driver.maximize_window()
    driver.find_element(By.ID, value="user_email").send_keys(os.getenv("BUNPRO_EMAIL"))
    pass_field = driver.find_element(By.ID, value="user_password")
    pass_field.send_keys(os.getenv("BUNPRO_PASSWORD"))
    pass_field.send_keys(Keys.ENTER)
    time.sleep(5)


def set_learnt(item):
    time.sleep(0.3)
    item.find_element(By.CLASS_NAME, value="dropdown-toggle").click()
    time.sleep(0.3)
    buttons = item.find_elements(By.CSS_SELECTOR, value="div.dropdown-menu li.u-flex")
    for button in buttons:
        if button.text == "Mark as Mastered":
            button.click()


def edit_deck(page, stop_page, deck):
    driver.get(f"https://bunpro.jp/decks/{deck}?page={str(page)}")
    page_start_time = time.time()
    time.sleep(5)
    if stop_page == 0:
        stop_page = int(driver.find_elements(By.CSS_SELECTOR, value="nav.pagy-nav span.page")[-2].text)
        print(stop_page)
        time.sleep(5)
    items = driver.find_elements(By.CLASS_NAME, value="deck-info-card")
    for item in items:
        srs_stage = item.find_elements(By.CSS_SELECTOR, value="div.u-flex.u-items_center")[-1].text
        vocab = item.find_element(By.CLASS_NAME, value="deck-card-title").text.split("\n")
        if len(vocab) <= 2:
            vocab = vocab[0]
        else:
            vocab = f"{vocab[0]}{vocab[-1]}"
        print(f"working on {vocab} with SRS: {srs_stage}")

        if vocab in imported_vocab_list and srs_stage != "SRS 12":
            print(f"{vocab}should be mastered")
            set_learnt(item)
            mastered_vocab.append(vocab)
        else:
            print(f"{vocab} not known")
    page_end_time = time.time()
    print(f"Page {page} took {page_end_time - page_start_time} seconds")
    print(f"Program has been running for {time.time() - start_time} seconds")
    time.sleep(2)
    if page < stop_page:
        edit_deck(page + 1, stop_page, deck)


def get_vocab():
    global imported_vocab_list
    imported_vocab_list = pd.read_csv("vocab.csv")["Vocab"].to_list()
    with open("test.txt", encoding='utf-8') as file:
        content = file.readlines()

    words = [re.sub("[\(\[\{].*?[\)\]\}]", "", word.replace('"', "").strip()) for word in content]
    for word in words:
        word = word.replace("\ufeff", "").split(" ")
        for entry in word:
            imported_vocab_list.append(entry)

    print(f"{imported_vocab_list}\nThese are the words, that will be set to known.\nThey are {len(imported_vocab_list)} words")

start_time = time.time()
get_vocab()
STARTING_PAGE = int(input("On what page do you want to start? Smallest is 1: "))
END_PAGE = int(input("On what page do you want to end? If you want every page enter 0; Max is 20: "))

login()
"resqiy/Bunpro-N5-Vocab", "lh0vxb/Bunpro-N4-Vocab"

DECKS = ["mvt76c/Bunpro-N3-Vocab",
         "dxbsvk/Bunpro-N2-Vocab", "qqovik/Bunpro-N1-Vocab"]

DECK = "Bunpro-N2-Vocab"

for deck in DECKS:
    start_mastered = len(mastered_vocab)
    edit_deck(STARTING_PAGE, END_PAGE, deck)
    print(f"Mastered {len(mastered_vocab) - start_mastered} in deck {deck.split("/")[1]}")

print(f"Mastered {len(mastered_vocab)} items")
print(mastered_vocab)

