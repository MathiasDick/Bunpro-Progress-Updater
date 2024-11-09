# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vocab_list.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import Resources_rc

class Ui_w_Vocab_List(object):
    def setupUi(self, w_Vocab_List):
        if not w_Vocab_List.objectName():
            w_Vocab_List.setObjectName(u"w_Vocab_List")
        w_Vocab_List.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/Vocab Window/anki.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_Vocab_List.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_Vocab_List)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_close = QPushButton(w_Vocab_List)
        self.pb_close.setObjectName(u"pb_close")

        self.gridLayout.addWidget(self.pb_close, 2, 1, 1, 1)

        self.lw_vocab = QListWidget(w_Vocab_List)
        self.lw_vocab.setObjectName(u"lw_vocab")

        self.gridLayout.addWidget(self.lw_vocab, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.l_known_vocab = QLabel(w_Vocab_List)
        self.l_known_vocab.setObjectName(u"l_known_vocab")

        self.gridLayout.addWidget(self.l_known_vocab, 0, 0, 1, 1)


        self.retranslateUi(w_Vocab_List)

        QMetaObject.connectSlotsByName(w_Vocab_List)
    # setupUi

    def retranslateUi(self, w_Vocab_List):
        w_Vocab_List.setWindowTitle(QCoreApplication.translate("w_Vocab_List", u"Vocab List", None))
        self.pb_close.setText(QCoreApplication.translate("w_Vocab_List", u"Close", None))
        self.l_known_vocab.setText(QCoreApplication.translate("w_Vocab_List", u"Known Vocab", None))
    # retranslateUi

