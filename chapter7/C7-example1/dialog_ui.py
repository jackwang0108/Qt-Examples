# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(493, 357)
        font = QFont()
        font.setFamilies([u"Hiragino Sans GB"])
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnClearText = QPushButton(self.groupBox_4)
        self.btnClearText.setObjectName(u"btnClearText")
        icon = QIcon()
        icon.addFile(u":/icons/images/212.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClearText.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnClearText)

        self.btnClose = QPushButton(self.groupBox_4)
        self.btnClose.setObjectName(u"btnClose")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/132.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnClose)


        self.gridLayout_4.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btnInputString = QPushButton(self.groupBox_3)
        self.btnInputString.setObjectName(u"btnInputString")

        self.gridLayout_3.addWidget(self.btnInputString, 0, 0, 1, 1)

        self.btnInputInt = QPushButton(self.groupBox_3)
        self.btnInputInt.setObjectName(u"btnInputInt")

        self.gridLayout_3.addWidget(self.btnInputInt, 0, 1, 1, 1)

        self.btnInputFloat = QPushButton(self.groupBox_3)
        self.btnInputFloat.setObjectName(u"btnInputFloat")

        self.gridLayout_3.addWidget(self.btnInputFloat, 1, 0, 1, 1)

        self.btnInputItem = QPushButton(self.groupBox_3)
        self.btnInputItem.setObjectName(u"btnInputItem")

        self.gridLayout_3.addWidget(self.btnInputItem, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btnMsgQuestion = QPushButton(self.groupBox_2)
        self.btnMsgQuestion.setObjectName(u"btnMsgQuestion")

        self.gridLayout_2.addWidget(self.btnMsgQuestion, 0, 0, 1, 1)

        self.btnMsgInformation = QPushButton(self.groupBox_2)
        self.btnMsgInformation.setObjectName(u"btnMsgInformation")

        self.gridLayout_2.addWidget(self.btnMsgInformation, 0, 1, 1, 1)

        self.btnMsgWarning = QPushButton(self.groupBox_2)
        self.btnMsgWarning.setObjectName(u"btnMsgWarning")

        self.gridLayout_2.addWidget(self.btnMsgWarning, 1, 0, 1, 1)

        self.btnMsgCritical = QPushButton(self.groupBox_2)
        self.btnMsgCritical.setObjectName(u"btnMsgCritical")

        self.gridLayout_2.addWidget(self.btnMsgCritical, 1, 1, 1, 1)

        self.btnMsgAbout = QPushButton(self.groupBox_2)
        self.btnMsgAbout.setObjectName(u"btnMsgAbout")

        self.gridLayout_2.addWidget(self.btnMsgAbout, 2, 0, 1, 1)

        self.btnMsgAboutQt = QPushButton(self.groupBox_2)
        self.btnMsgAboutQt.setObjectName(u"btnMsgAboutQt")

        self.gridLayout_2.addWidget(self.btnMsgAboutQt, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(220, 0))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.btnSelDir = QPushButton(self.groupBox)
        self.btnSelDir.setObjectName(u"btnSelDir")

        self.gridLayout.addWidget(self.btnSelDir, 1, 0, 1, 1)

        self.btnColor = QPushButton(self.groupBox)
        self.btnColor.setObjectName(u"btnColor")

        self.gridLayout.addWidget(self.btnColor, 2, 0, 1, 1)

        self.btnOpen = QPushButton(self.groupBox)
        self.btnOpen.setObjectName(u"btnOpen")

        self.gridLayout.addWidget(self.btnOpen, 0, 0, 1, 1)

        self.btnSave = QPushButton(self.groupBox)
        self.btnSave.setObjectName(u"btnSave")

        self.gridLayout.addWidget(self.btnSave, 1, 1, 1, 1)

        self.btnFont = QPushButton(self.groupBox)
        self.btnFont.setObjectName(u"btnFont")

        self.gridLayout.addWidget(self.btnFont, 2, 1, 1, 1)

        self.btnOpenMulti = QPushButton(self.groupBox)
        self.btnOpenMulti.setObjectName(u"btnOpenMulti")

        self.gridLayout.addWidget(self.btnOpenMulti, 0, 1, 1, 1)

        self.btnProgress = QPushButton(self.groupBox)
        self.btnProgress.setObjectName(u"btnProgress")

        self.gridLayout.addWidget(self.btnProgress, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        self.plainTextEdit.setFont(font1)

        self.verticalLayout.addWidget(self.plainTextEdit)

        QWidget.setTabOrder(self.btnOpen, self.btnOpenMulti)
        QWidget.setTabOrder(self.btnOpenMulti, self.btnSelDir)
        QWidget.setTabOrder(self.btnSelDir, self.btnSave)
        QWidget.setTabOrder(self.btnSave, self.btnColor)
        QWidget.setTabOrder(self.btnColor, self.btnFont)
        QWidget.setTabOrder(self.btnFont, self.btnMsgQuestion)
        QWidget.setTabOrder(self.btnMsgQuestion, self.btnMsgInformation)
        QWidget.setTabOrder(self.btnMsgInformation, self.btnInputString)
        QWidget.setTabOrder(self.btnInputString, self.btnInputInt)
        QWidget.setTabOrder(self.btnInputInt, self.btnInputFloat)
        QWidget.setTabOrder(self.btnInputFloat, self.btnInputItem)
        QWidget.setTabOrder(self.btnInputItem, self.btnClearText)
        QWidget.setTabOrder(self.btnClearText, self.plainTextEdit)

        self.retranslateUi(Dialog)
        self.btnClose.clicked.connect(Dialog.close)
        self.btnClearText.clicked.connect(self.plainTextEdit.clear)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6807\u51c6\u5bf9\u8bdd\u6846\u7684\u4f7f\u7528", None))
        self.groupBox_4.setTitle("")
        self.btnClearText.setText(QCoreApplication.translate("Dialog", u"\u6e05\u9664\u6587\u672c\u6846\u5185\u5bb9", None))
        self.btnClose.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u6807\u51c6\u8f93\u5165\u5bf9\u8bdd\u6846 QInputDialog", None))
        self.btnInputString.setText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u5b57\u7b26\u4e32", None))
        self.btnInputInt.setText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u6574\u6570", None))
        self.btnInputFloat.setText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u6d6e\u70b9\u6570", None))
        self.btnInputItem.setText(QCoreApplication.translate("Dialog", u"\u6761\u76ee\u9009\u62e9\u8f93\u5165", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u6807\u51c6\u6d88\u606f\u6846 QMessageBox", None))
        self.btnMsgQuestion.setText(QCoreApplication.translate("Dialog", u"question", None))
        self.btnMsgInformation.setText(QCoreApplication.translate("Dialog", u"information", None))
        self.btnMsgWarning.setText(QCoreApplication.translate("Dialog", u"warning", None))
        self.btnMsgCritical.setText(QCoreApplication.translate("Dialog", u"critical", None))
        self.btnMsgAbout.setText(QCoreApplication.translate("Dialog", u"about", None))
        self.btnMsgAboutQt.setText(QCoreApplication.translate("Dialog", u"aboutQt", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6807\u51c6\u5bf9\u8bdd\u6846", None))
        self.btnSelDir.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u5df2\u6709\u76ee\u5f55", None))
        self.btnColor.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u989c\u8272", None))
        self.btnOpen.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u4e00\u4e2a\u6587\u4ef6", None))
        self.btnSave.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.btnFont.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u5b57\u4f53", None))
        self.btnOpenMulti.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u591a\u4e2a\u6587\u4ef6", None))
        self.btnProgress.setText(QCoreApplication.translate("Dialog", u"\u8fdb\u5ea6\u5bf9\u8bdd\u6846", None))
    # retranslateUi

