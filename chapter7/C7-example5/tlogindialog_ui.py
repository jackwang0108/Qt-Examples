# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tlogindialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_TLoginDialog(object):
    def setupUi(self, TLoginDialog):
        if not TLoginDialog.objectName():
            TLoginDialog.setObjectName(u"TLoginDialog")
        TLoginDialog.resize(642, 316)
        self.verticalLayout = QVBoxLayout(TLoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(TLoginDialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/images/splash2.jpg"))

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(TLoginDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEditUserName = QLineEdit(TLoginDialog)
        self.lineEditUserName.setObjectName(u"lineEditUserName")

        self.horizontalLayout.addWidget(self.lineEditUserName)

        self.label_3 = QLabel(TLoginDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEditUserPass = QLineEdit(TLoginDialog)
        self.lineEditUserPass.setObjectName(u"lineEditUserPass")
        self.lineEditUserPass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.lineEditUserPass)

        self.checkBox = QCheckBox(TLoginDialog)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOk = QPushButton(TLoginDialog)
        self.btnOk.setObjectName(u"btnOk")

        self.horizontalLayout.addWidget(self.btnOk)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(TLoginDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TLoginDialog)
        self.btnCancel.clicked.connect(TLoginDialog.close)

        QMetaObject.connectSlotsByName(TLoginDialog)
    # setupUi

    def retranslateUi(self, TLoginDialog):
        TLoginDialog.setWindowTitle(QCoreApplication.translate("TLoginDialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("TLoginDialog", u"\u7528\u6237\u540d", None))
        self.lineEditUserName.setPlaceholderText(QCoreApplication.translate("TLoginDialog", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("TLoginDialog", u"\u5bc6\u7801", None))
        self.lineEditUserPass.setText("")
        self.lineEditUserPass.setPlaceholderText(QCoreApplication.translate("TLoginDialog", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.checkBox.setText(QCoreApplication.translate("TLoginDialog", u"\u4fdd\u5b58\u7528\u6237", None))
        self.btnOk.setText(QCoreApplication.translate("TLoginDialog", u"\u786e\u5b9a", None))
        self.btnCancel.setText(QCoreApplication.translate("TLoginDialog", u"\u53d6\u6d88", None))
    # retranslateUi

