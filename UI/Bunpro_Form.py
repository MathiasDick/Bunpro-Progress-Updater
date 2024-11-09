# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bunpro_Form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
import Resources_rc

class Ui_w_Bunpro(object):
    def setupUi(self, w_Bunpro):
        if not w_Bunpro.objectName():
            w_Bunpro.setObjectName(u"w_Bunpro")
        w_Bunpro.resize(616, 524)
        icon = QIcon()
        icon.addFile(u":/Main Window/bunpro-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_Bunpro.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_Bunpro)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(w_Bunpro)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_wanikani_api = QLineEdit(self.groupBox)
        self.le_wanikani_api.setObjectName(u"le_wanikani_api")

        self.gridLayout_2.addWidget(self.le_wanikani_api, 0, 1, 1, 1)

        self.pb_wanikani_select = QPushButton(self.groupBox)
        self.pb_wanikani_select.setObjectName(u"pb_wanikani_select")

        self.gridLayout_2.addWidget(self.pb_wanikani_select, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.le_wanikani_file = QLineEdit(self.groupBox)
        self.le_wanikani_file.setObjectName(u"le_wanikani_file")

        self.gridLayout_2.addWidget(self.le_wanikani_file, 1, 1, 1, 1)

        self.pb_wanikani_api_import = QPushButton(self.groupBox)
        self.pb_wanikani_api_import.setObjectName(u"pb_wanikani_api_import")

        self.gridLayout_2.addWidget(self.pb_wanikani_api_import, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lb_wanikani_message = QLabel(self.groupBox)
        self.lb_wanikani_message.setObjectName(u"lb_wanikani_message")
        self.lb_wanikani_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_wanikani_message, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(w_Bunpro)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.le_anki_file = QLineEdit(self.groupBox_2)
        self.le_anki_file.setObjectName(u"le_anki_file")

        self.gridLayout_4.addWidget(self.le_anki_file, 0, 1, 1, 1)

        self.pb_anki_select = QPushButton(self.groupBox_2)
        self.pb_anki_select.setObjectName(u"pb_anki_select")

        self.gridLayout_4.addWidget(self.pb_anki_select, 0, 2, 1, 1)

        self.lb_anki_message = QLabel(self.groupBox_2)
        self.lb_anki_message.setObjectName(u"lb_anki_message")
        self.lb_anki_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_anki_message, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(w_Bunpro)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cb_n2 = QCheckBox(self.frame)
        self.cb_n2.setObjectName(u"cb_n2")

        self.gridLayout_5.addWidget(self.cb_n2, 0, 4, 1, 1)

        self.cb_all = QCheckBox(self.frame)
        self.cb_all.setObjectName(u"cb_all")

        self.gridLayout_5.addWidget(self.cb_all, 0, 6, 1, 1)

        self.cb_n4 = QCheckBox(self.frame)
        self.cb_n4.setObjectName(u"cb_n4")

        self.gridLayout_5.addWidget(self.cb_n4, 0, 2, 1, 1)

        self.cb_n3 = QCheckBox(self.frame)
        self.cb_n3.setObjectName(u"cb_n3")

        self.gridLayout_5.addWidget(self.cb_n3, 0, 3, 1, 1)

        self.cb_n1 = QCheckBox(self.frame)
        self.cb_n1.setObjectName(u"cb_n1")

        self.gridLayout_5.addWidget(self.cb_n1, 0, 5, 1, 1)

        self.cb_n5 = QCheckBox(self.frame)
        self.cb_n5.setObjectName(u"cb_n5")

        self.gridLayout_5.addWidget(self.cb_n5, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.groupBox_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.sb_starting_page = QSpinBox(self.frame_2)
        self.sb_starting_page.setObjectName(u"sb_starting_page")
        self.sb_starting_page.setMinimum(1)
        self.sb_starting_page.setMaximum(20)

        self.gridLayout_3.addWidget(self.sb_starting_page, 0, 1, 1, 1)

        self.sb_ending_page = QSpinBox(self.frame_2)
        self.sb_ending_page.setObjectName(u"sb_ending_page")

        self.gridLayout_3.addWidget(self.sb_ending_page, 0, 4, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.cb_all_pages = QCheckBox(self.groupBox_3)
        self.cb_all_pages.setObjectName(u"cb_all_pages")

        self.verticalLayout.addWidget(self.cb_all_pages)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.le_bunpro_email = QLineEdit(self.groupBox_4)
        self.le_bunpro_email.setObjectName(u"le_bunpro_email")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_bunpro_email)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.le_bunpro_password = QLineEdit(self.groupBox_4)
        self.le_bunpro_password.setObjectName(u"le_bunpro_password")
        self.le_bunpro_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_bunpro_password)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.pb_check_vocab = QPushButton(self.groupBox_3)
        self.pb_check_vocab.setObjectName(u"pb_check_vocab")

        self.verticalLayout.addWidget(self.pb_check_vocab)

        self.pb_start_bot = QPushButton(self.groupBox_3)
        self.pb_start_bot.setObjectName(u"pb_start_bot")

        self.verticalLayout.addWidget(self.pb_start_bot)

        self.lb_bot_message = QLabel(self.groupBox_3)
        self.lb_bot_message.setObjectName(u"lb_bot_message")
        self.lb_bot_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_bot_message)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.retranslateUi(w_Bunpro)

        QMetaObject.connectSlotsByName(w_Bunpro)
    # setupUi

    def retranslateUi(self, w_Bunpro):
        w_Bunpro.setWindowTitle(QCoreApplication.translate("w_Bunpro", u"Bunpro Progress Updater | by Mathias Dick", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_Bunpro", u"Import vocab from Wanikani", None))
        self.pb_wanikani_select.setText(QCoreApplication.translate("w_Bunpro", u"Select", None))
        self.label_3.setText(QCoreApplication.translate("w_Bunpro", u"Select Wanikani vocab on disk", None))
        self.pb_wanikani_api_import.setText(QCoreApplication.translate("w_Bunpro", u"Save vocab on disk", None))
        self.label.setText(QCoreApplication.translate("w_Bunpro", u"Enter your Wanikani API key", None))
        self.lb_wanikani_message.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("w_Bunpro", u"Import vocab from Anki", None))
        self.label_4.setText(QCoreApplication.translate("w_Bunpro", u"Select Anki vocab on disk", None))
        self.pb_anki_select.setText(QCoreApplication.translate("w_Bunpro", u"Select", None))
        self.lb_anki_message.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("w_Bunpro", u"Set progress on Bunpro", None))
        self.cb_n2.setText(QCoreApplication.translate("w_Bunpro", u"N2", None))
        self.cb_all.setText(QCoreApplication.translate("w_Bunpro", u"All", None))
        self.cb_n4.setText(QCoreApplication.translate("w_Bunpro", u"N4", None))
        self.cb_n3.setText(QCoreApplication.translate("w_Bunpro", u"N3", None))
        self.cb_n1.setText(QCoreApplication.translate("w_Bunpro", u"N1", None))
        self.cb_n5.setText(QCoreApplication.translate("w_Bunpro", u"N5", None))
        self.label_2.setText(QCoreApplication.translate("w_Bunpro", u"Select the decks you want to update", None))
        self.label_5.setText(QCoreApplication.translate("w_Bunpro", u"Starting page:", None))
        self.label_6.setText(QCoreApplication.translate("w_Bunpro", u"Ending page:", None))
        self.cb_all_pages.setText(QCoreApplication.translate("w_Bunpro", u"Go through all pages", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("w_Bunpro", u"Bunpro login", None))
        self.label_7.setText(QCoreApplication.translate("w_Bunpro", u"Email:", None))
        self.label_8.setText(QCoreApplication.translate("w_Bunpro", u"Password:", None))
        self.pb_check_vocab.setText(QCoreApplication.translate("w_Bunpro", u"Check known vocab", None))
        self.pb_start_bot.setText(QCoreApplication.translate("w_Bunpro", u"Start bot", None))
        self.lb_bot_message.setText("")
    # retranslateUi

