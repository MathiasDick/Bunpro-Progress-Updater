import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.Bunpro_Form import Ui_w_Bunpro
from UI.Vocab_list import Ui_w_Vocab_List
import web_interaction


class Bunpro(qtw.QWidget, Ui_w_Bunpro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.vocab_window = None

        self.pb_wanikani_api_import.clicked.connect(self.wanikani_api_import)
        self.pb_wanikani_select.clicked.connect(self.wanikani_import)
        self.pb_anki_select.clicked.connect(self.anki_import)

        self.cb_all.stateChanged.connect(self.switch_checkbox)
        self.cb_all_pages.stateChanged.connect(self.switch_page_select)
        self.pb_start_bot.clicked.connect(self.start_bot)
        self.pb_check_vocab.clicked.connect(self.check_vocab)

        self.le_anki_file.setText("files/anki_vocab.txt")
        self.le_wanikani_file.setText("files/wanikani_vocab.csv")

    @qtc.Slot()
    def wanikani_api_import(self):
        api =  self.le_wanikani_api.text()
        wanikani = web_interaction.Wanikani(api)
        wanikani.create_list()
        self.lb_wanikani_message.setText("Successfully imported!")

    @qtc.Slot()
    def wanikani_import(self):
        dialog = qtw.QFileDialog()
        dialog.setNameFilter("*.csv")
        dialog_successful = dialog.exec()

        if dialog_successful:
            self.wanikani_file = dialog.selectedFiles()[0]
            self.le_wanikani_file.setText(self.wanikani_file)

    @qtc.Slot()
    def anki_import(self):
        dialog = qtw.QFileDialog()
        dialog.setNameFilter("*.txt")
        dialog_successful = dialog.exec()

        if dialog_successful:
            self.anki_file = dialog.selectedFiles()[0]
            self.le_anki_file.setText(self.anki_file)

    @qtc.Slot()
    def switch_checkbox(self):
        if self.cb_all.isChecked():
            self.cb_n1.setChecked(True)
            self.cb_n2.setChecked(True)
            self.cb_n3.setChecked(True)
            self.cb_n4.setChecked(True)
            self.cb_n5.setChecked(True)
        else:
            self.cb_n1.setChecked(False)
            self.cb_n2.setChecked(False)
            self.cb_n3.setChecked(False)
            self.cb_n4.setChecked(False)
            self.cb_n5.setChecked(False)

    @qtc.Slot()
    def switch_page_select(self):
        self.sb_starting_page.setValue(1)
        self.sb_ending_page.setValue(0)
        if self.cb_all_pages.isChecked():
            self.sb_starting_page.setDisabled(True)
            self.sb_ending_page.setDisabled(True)
        else:
            self.sb_starting_page.setDisabled(False)
            self.sb_ending_page.setDisabled(False)

    @qtc.Slot()
    def start_bot(self):
        start_page = self.sb_starting_page.value()
        end_page = self.sb_ending_page.value()
        decks = []
        decks.append("qqovik/Bunpro-N1-Vocab") if self.cb_n1.isChecked() else 0
        decks.append("dxbsvk/Bunpro-N2-Vocab") if self.cb_n2.isChecked() else 0
        decks.append("mvt76c/Bunpro-N3-Vocab") if self.cb_n3.isChecked() else 0
        decks.append("lh0vxb/Bunpro-N4-Vocab") if self.cb_n4.isChecked() else 0
        decks.append("resqiy/Bunpro-N5-Vocab") if self.cb_n5.isChecked() else 0

        bunpro.get_vocab(self.le_wanikani_file.text(), self.le_anki_file.text())

        bunpro.login()

        for deck in decks:
            print(deck)
            start_mastered = len(bunpro.mastered_vocab)
            bunpro.edit_deck(start_page, end_page, deck)
            print(f"Mastered {len(bunpro.mastered_vocab) - start_mastered} in deck {deck.split("/")[1]}")

        print(f"Mastered {len(bunpro.mastered_vocab)} items")
        print(bunpro.mastered_vocab)

    @qtc.Slot()
    def check_vocab(self):
        bunpro.get_vocab(self.le_wanikani_file.text(), self.le_anki_file.text())
        if self.vocab_window is None or not self.vocab_window.isVisible():
            self.vocab_window = CheckVocab()
        self.vocab_window.lw_vocab.addItems(bunpro.imported_vocab_list)
        self.vocab_window.l_known_vocab.setText(f"You know {len(bunpro.imported_vocab_list)} Words. All of these will be set as mastered in Bunpro")
        self.vocab_window.show()

class CheckVocab(qtw.QWidget, Ui_w_Vocab_List):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show()
        self.pb_close.clicked.connect(self.close)





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    bunpro = web_interaction.Bunpro()

    window = Bunpro()
    window.show()

    sys.exit(app.exec())