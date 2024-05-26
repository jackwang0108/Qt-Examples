# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(589, 639)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.editStr = QLineEdit(self.groupBox)
        self.editStr.setObjectName(u"editStr")

        self.gridLayout.addWidget(self.editStr, 0, 1, 1, 1)

        self.btnGetChars = QPushButton(self.groupBox)
        self.btnGetChars.setObjectName(u"btnGetChars")

        self.gridLayout.addWidget(self.btnGetChars, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.editChar = QLineEdit(self.groupBox)
        self.editChar.setObjectName(u"editChar")

        self.gridLayout.addWidget(self.editChar, 1, 1, 1, 1)

        self.btnCharJudge = QPushButton(self.groupBox)
        self.btnCharJudge.setObjectName(u"btnCharJudge")

        self.gridLayout.addWidget(self.btnCharJudge, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnLatin1 = QPushButton(self.groupBox_2)
        self.btnLatin1.setObjectName(u"btnLatin1")

        self.gridLayout_2.addWidget(self.btnLatin1, 0, 0, 1, 1)

        self.btnUTF16 = QPushButton(self.groupBox_2)
        self.btnUTF16.setObjectName(u"btnUTF16")

        self.gridLayout_2.addWidget(self.btnUTF16, 0, 1, 1, 1)

        self.btnCompare = QPushButton(self.groupBox_2)
        self.btnCompare.setObjectName(u"btnCompare")

        self.gridLayout_2.addWidget(self.btnCompare, 1, 0, 1, 1)

        self.btnClear = QPushButton(self.groupBox_2)
        self.btnClear.setObjectName(u"btnClear")

        self.gridLayout_2.addWidget(self.btnClear, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.chkDigit = QCheckBox(self.groupBox_4)
        self.chkDigit.setObjectName(u"chkDigit")

        self.gridLayout_4.addWidget(self.chkDigit, 0, 0, 1, 1)

        self.chkLetter = QCheckBox(self.groupBox_4)
        self.chkLetter.setObjectName(u"chkLetter")

        self.gridLayout_4.addWidget(self.chkLetter, 1, 0, 1, 1)

        self.chkLetterOrNumber = QCheckBox(self.groupBox_4)
        self.chkLetterOrNumber.setObjectName(u"chkLetterOrNumber")

        self.gridLayout_4.addWidget(self.chkLetterOrNumber, 2, 0, 1, 1)

        self.chkUpper = QCheckBox(self.groupBox_4)
        self.chkUpper.setObjectName(u"chkUpper")

        self.gridLayout_4.addWidget(self.chkUpper, 3, 0, 1, 1)

        self.chkLowe = QCheckBox(self.groupBox_4)
        self.chkLowe.setObjectName(u"chkLowe")

        self.gridLayout_4.addWidget(self.chkLowe, 4, 0, 1, 1)

        self.chkMark = QCheckBox(self.groupBox_4)
        self.chkMark.setObjectName(u"chkMark")

        self.gridLayout_4.addWidget(self.chkMark, 5, 0, 1, 1)

        self.chkSpace = QCheckBox(self.groupBox_4)
        self.chkSpace.setObjectName(u"chkSpace")

        self.gridLayout_4.addWidget(self.chkSpace, 6, 0, 1, 1)

        self.chkSymbol = QCheckBox(self.groupBox_4)
        self.chkSymbol.setObjectName(u"chkSymbol")

        self.gridLayout_4.addWidget(self.chkSymbol, 7, 0, 1, 1)

        self.chkPunct = QCheckBox(self.groupBox_4)
        self.chkPunct.setObjectName(u"chkPunct")

        self.gridLayout_4.addWidget(self.chkPunct, 8, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u5b57\u7b26\u4e32", None))
        self.btnGetChars.setText(QCoreApplication.translate("Widget", u"\u6bcf\u4e2a\u5b57\u7b26\u7684Unicode", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u5355\u4e2a\u5b57\u7b26", None))
        self.btnCharJudge.setText(QCoreApplication.translate("Widget", u"\u5355\u4e2a\u5b57\u7b26\u7684\u7279\u6027\u5224\u65ad", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5176\u4ed6\u6d4b\u8bd5\u548c\u529f\u80fd", None))
        self.btnLatin1.setText(QCoreApplication.translate("Widget", u"\u4e0eLatin-1\u7684\u8f6c\u6362", None))
        self.btnUTF16.setText(QCoreApplication.translate("Widget", u"\u4e0eUTF-16\u7684\u8f6c\u6362", None))
        self.btnCompare.setText(QCoreApplication.translate("Widget", u"QChar\u7684\u6bd4\u8f83\u548c\u66ff\u6362", None))
        self.btnClear.setText(QCoreApplication.translate("Widget", u"\u6e05\u7a7a\u6587\u672c\u6846", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u663e\u793a\u7ed3\u679c", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"QChar\u7279\u6027\u5224\u65ad", None))
        self.chkDigit.setText(QCoreApplication.translate("Widget", u"isDigit", None))
        self.chkLetter.setText(QCoreApplication.translate("Widget", u"isLetter", None))
        self.chkLetterOrNumber.setText(QCoreApplication.translate("Widget", u"isLetterOrNumber", None))
        self.chkUpper.setText(QCoreApplication.translate("Widget", u"isUpper", None))
        self.chkLowe.setText(QCoreApplication.translate("Widget", u"isLower", None))
        self.chkMark.setText(QCoreApplication.translate("Widget", u"isMark", None))
        self.chkSpace.setText(QCoreApplication.translate("Widget", u"isSpace", None))
        self.chkSymbol.setText(QCoreApplication.translate("Widget", u"isSymbol", None))
        self.chkPunct.setText(QCoreApplication.translate("Widget", u"isPunct", None))
    # retranslateUi

