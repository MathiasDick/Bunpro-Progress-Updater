import logging
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import wanikani_api.client
from UI.Bunpro_Form import Ui_w_Bunpro


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Bunpro:
    def __init__(self, gui):
        self.start_time = None
        self.driver = None
        self.chrome_options = None
        self.bunpro_gui : Ui_w_Bunpro = gui
        self.imported_vocab_list = []
        self.mastered_vocab = []



    def login(self):
        """Logs user into Bunpro using provided credentials"""
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_experimental_option("detach", True)
            self.chrome_options.add_argument("--disable-search-engine-choice-screen")
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.start_time = time.time()
            self.driver.get("https://bunpro.jp/login")
            self.driver.maximize_window()

            # Wait until login form is present
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
            logging.info("Login page loaded.")

            # Fill login form with credentials
            self.driver.find_element(By.CSS_SELECTOR, value="input#user_email").click()
            self.driver.find_element(By.CSS_SELECTOR, value="input#user_email").send_keys(self.bunpro_gui.le_bunpro_email.text())
            pass_field = self.driver.find_element(By.ID, value="user_password")
            pass_field.send_keys(self.bunpro_gui.le_bunpro_password.text())
            pass_field.send_keys(Keys.ENTER)

            # Wait until the user is logged in and the main page loads
            WebDriverWait(self.driver, 10).until(EC.url_contains("https://bunpro.jp/dashboard"))
            logging.info("Logged into Bunpro successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error("Login failed: %s", e)
            self.bunpro_gui.lb_bot_message.setText("Login failed. Please check your credentials.")

    def get_vocab(self, wanikani_file, anki_file):
        """Add all the known Vocabulary listed in the wanikani_vocab.csv from Wanikani and anki_vocab.txt from Anki ot the imported_vocab_list"""
        # Import Wanikani vocab
        try:
            self.imported_vocab_list = pd.read_csv(wanikani_file)["Vocab"].to_list()
            self.bunpro_gui.lb_wanikani_message.setText("Wanikani file successfully imported")
            logging.info("Wanikani vocabulary imported.")
        except Exception as e:
            logging.error("Failed to import Wanikani vocabulary: %s", e)
            self.bunpro_gui.lb_wanikani_message.setText("No Wanikani file found")

        # Import Anki vocab
        try:
            with open(anki_file, encoding='utf-8') as file:
                content = file.readlines()
            words = [re.sub("[\(\[\{].*?[\)\]\}]", "", word.replace('"', "").strip()) for word in content]
            for word in words:
                word = word.replace("\ufeff", "").split(" ")
                for entry in word:
                    self.imported_vocab_list.append(entry)
            self.bunpro_gui.lb_anki_message.setText("Anki file successfully imported")
            logging.info("Anki vocabulary imported.")
        except Exception as e:
            logging.error("Failed to import Anki vocabulary: %s", e)
            self.bunpro_gui.lb_anki_message.setText("No Anki file found")

    def set_learnt(self, item):
        """Marks an item as mastered in the Bunpro vocabulary list"""
        try:
            # Open item dropdown to select "Mark as Mastered"
            item.find_element(By.CLASS_NAME, value="dropdown-toggle").click()
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.dropdown-menu li.u-flex"))
            )
            buttons = item.find_elements(By.CSS_SELECTOR, "div.dropdown-menu li.u-flex")
            for button in buttons:
                if button.text == "Mark as Mastered":
                    button.click()
                    break
            logging.info("Marked item as mastered.")
        except NoSuchElementException:
            logging.warning("Could not find the mastery option for this item.")
        except TimeoutException:
            logging.warning("Dropdown for mastery option did not load in time.")


    def edit_deck(self, page, stop_page, deck):
        """Navigates through deck pages to mark vocabulary as mastered"""
        try:
            # Load deck page
            self.driver.get(f"https://bunpro.jp/decks/{deck}?page={str(page)}")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "deck-info-card"))
            )
            logging.info("Navigated to page %d of deck %s.", page, deck)

            if stop_page == 0:
                stop_page = int(self.driver.find_elements(By.CSS_SELECTOR, "nav.pagy-nav span.page")[-2].text)
                logging.info("Identified last page as %d.", stop_page)

            # Process each vocabulary item on the page
            items = self.driver.find_elements(By.CLASS_NAME, "deck-info-card")
            for item in items:
                srs_stage = item.find_elements(By.CSS_SELECTOR, "div.u-flex.u-items_center")[-1].text
                vocab = item.find_element(By.CLASS_NAME, "deck-card-title").text.split("\n")
                vocab = vocab[0] if len(vocab) <= 2 else f"{vocab[0]}{vocab[-1]}"
                logging.info("Processing vocab %s with SRS stage %s", vocab, srs_stage)

                if vocab in self.imported_vocab_list and srs_stage != "SRS 12":
                    self.set_learnt(item)
                    self.mastered_vocab.append(vocab)
                elif srs_stage == "SRS 12":
                    logging.info("%s already mastered", vocab)
                else:
                    logging.info("%s not known", vocab)

            if page < stop_page:
                self.edit_deck(page + 1, stop_page, deck)
        except (NoSuchElementException, TimeoutException) as e:
            logging.error("Failed to load or process page %d of deck %s: %s", page, deck, e)


class Wanikani:
    def __init__(self, api):
        self.df = pd.DataFrame()
        self.wanikani_api = api
        self.client = wanikani_api.client.Client(self.wanikani_api)
        self.words = []
        self.mean = []

    def create_list(self, bunpro_gui : Ui_w_Bunpro):
        """Fetches vocabulary from Wanikani API and saves it to a CSV file"""
        try:
            all_vocabulary = self.client.subjects(types="vocabulary", fetch_all=True)
            self.words = [word.characters for word in all_vocabulary]
            self.mean = [meaning.meanings[0].meaning for meaning in all_vocabulary]
            self.df["Vocab"] = self.words
            self.df["Meaning"] = self.mean
            self.df.to_csv("files/wanikani_vocab.csv", index=False)
            bunpro_gui.lb_wanikani_message.setText("Wanikani file successfully created")
            logging.info("Wanikani vocabulary file created.")
        except Exception as e:
            logging.error("Failed to create Wanikani vocabulary list: %s", e)
            bunpro_gui.lb_wanikani_message.setText("Failed to create Wanikani file")


