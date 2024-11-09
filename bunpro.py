import sys
import logging
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from UI.Bunpro_Form import Ui_w_Bunpro
from UI.Vocab_list import Ui_w_Vocab_List
import web_interaction

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Bunpro(qtw.QWidget, Ui_w_Bunpro):
    def __init__(self):
        super().__init__()
        self.anki_file = None
        self.setupUi(self)

        # Initialize vocab window
        self.vocab_window = None
        self.setup_buttons()

        # Set default file paths
        self.le_anki_file.setText("files/anki_vocab.txt")
        self.le_wanikani_file.setText("files/wanikani_vocab.csv")
        logging.info("UI initialized with default file paths.")

    def setup_buttons(self):
        """Sets up the buttons in the UI and connects them to event handlers."""
        # Button to import vocab from Wanikani API
        self.pb_wanikani_api_import.clicked.connect(self.wanikani_api_import)
        # Button to select Wanikani CSV file
        self.pb_wanikani_select.clicked.connect(self.select_wanikani_file)
        # Button to select Anki TXT file
        self.pb_anki_select.clicked.connect(self.select_anki_file)
        # Checkbox to toggle all JLPT levels
        self.cb_all.stateChanged.connect(self.toggle_all_levels)
        # Checkbox to enable or disable all page selections
        self.cb_all_pages.stateChanged.connect(self.toggle_page_selection)
        # Button to start the vocabulary bot
        self.pb_start_bot.clicked.connect(self.start_bot)
        # Button to check vocabulary list
        self.pb_check_vocab.clicked.connect(self.check_vocab)

    @qtc.Slot()
    def wanikani_api_import(self):
        """Imports vocabulary list from Wanikani API based on user's API key input."""
        try:
            api_key = self.le_wanikani_api.text()
            self.lb_wanikani_message.setText("Importing vocab from the Wanikani API...")
            wanikani = web_interaction.Wanikani(api_key)
            wanikani.create_list(self)
            self.lb_wanikani_message.setText("Successfully imported!")
            logging.info("Wanikani API vocab imported successfully.")
        except Exception as e:
            logging.error("Error during Wanikani API import: %s", e)
            self.lb_wanikani_message.setText("Failed to import from Wanikani API")

    @qtc.Slot()
    def select_wanikani_file(self):
        """Opens a file dialog for the user to select the Wanikani CSV vocabulary file."""
        dialog = qtw.QFileDialog()
        dialog.setNameFilter("*.csv")
        if dialog.exec():
            self.wanikani_file = dialog.selectedFiles()[0]
            self.le_wanikani_file.setText(self.wanikani_file)
            logging.info("Selected Wanikani file: %s", self.wanikani_file)

    @qtc.Slot()
    def toggle_all_levels(self):
        """Toggles the selection state of all JLPT level checkboxes."""
        state = self.cb_all.isChecked()
        for cb in [self.cb_n1, self.cb_n2, self.cb_n3, self.cb_n4, self.cb_n5]:
            cb.setChecked(state)
        logging.info("All JLPT levels %s", "selected" if state else "deselected")

    @qtc.Slot()
    def select_anki_file(self):
        """Opens a file dialog for the user to select the Anki TXT vocabulary file."""
        dialog = qtw.QFileDialog()
        dialog.setNameFilter("*.txt")
        if dialog.exec():
            self.anki_file = dialog.selectedFiles()[0]
            self.le_anki_file.setText(self.anki_file)
            logging.info("Selected Anki file: %s", self.anki_file)

    @qtc.Slot()
    def toggle_page_selection(self):
        """Enable or disable page selection fields based on the 'All Pages' checkbox."""
        state = self.cb_all_pages.isChecked()
        self.sb_starting_page.setValue(1)
        self.sb_ending_page.setValue(0)
        self.sb_starting_page.setDisabled(state)
        self.sb_ending_page.setDisabled(state)
        logging.info("Page selection %s", "disabled" if state else "enabled")

    @qtc.Slot()
    def start_bot(self):
        """Starts the vocabulary mastering bot based on user selections."""
        try:
            start_page = self.sb_starting_page.value()
            end_page = self.sb_ending_page.value()
            selected_decks = self.get_selected_decks()

            # Initialize Bunpro web interaction handler
            bunpro.get_vocab(self.le_wanikani_file.text(), self.le_anki_file.text())
            bunpro.login()


            # Iterate over each selected deck to master vocabulary
            for deck in selected_decks:
                start_mastered = len(bunpro.mastered_vocab)
                bunpro.edit_deck(start_page, end_page, deck)
                logging.info("Mastered %d items in deck %s", len(bunpro.mastered_vocab) - start_mastered, deck)

            self.lb_bot_message.setText(f"Bot is finished! Total number of newly mastered items: {len(bunpro.mastered_vocab)}")
            logging.info("Bot is finished! Total mastered items: %d", len(bunpro.mastered_vocab))
            bunpro.driver.close()
        except Exception as e:
            logging.error("Error starting bot: %s", e)
            self.lb_wanikani_message.setText("Failed to start bot")

    def get_selected_decks(self):
        """Returns a list of selected decks based on JLPT level checkboxes."""
        decks = []
        decks.append("qqovik/Bunpro-N1-Vocab") if self.cb_n1.isChecked() else 0
        decks.append("dxbsvk/Bunpro-N2-Vocab") if self.cb_n2.isChecked() else 0
        decks.append("mvt76c/Bunpro-N3-Vocab") if self.cb_n3.isChecked() else 0
        decks.append("lh0vxb/Bunpro-N4-Vocab") if self.cb_n4.isChecked() else 0
        decks.append("resqiy/Bunpro-N5-Vocab") if self.cb_n5.isChecked() else 0
        return decks


    @qtc.Slot()
    def check_vocab(self):
        """Opens a window to display the vocabulary list to be mastered."""
        try:
            bunpro.get_vocab(self.le_wanikani_file.text(), self.le_anki_file.text())

            if not self.vocab_window or not self.vocab_window.isVisible():
                self.vocab_window = CheckVocab()
                self.vocab_window.lw_vocab.addItems(bunpro.imported_vocab_list)
                vocab_count = len(bunpro.imported_vocab_list)
                self.vocab_window.l_known_vocab.setText(f"You know {vocab_count} words. All will be set as mastered in Bunpro")
                logging.info("Displayed known vocab list with %d items", vocab_count)
                self.vocab_window.show()
        except Exception as e:
            logging.error("Failed to check vocab: %s", e)
            self.lb_wanikani_message.setText("Failed to load vocab list")

class CheckVocab(qtw.QWidget, Ui_w_Vocab_List):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb_close.clicked.connect(self.close)





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Bunpro()
    bunpro = web_interaction.Bunpro(window)
    window.show()
    sys.exit(app.exec())