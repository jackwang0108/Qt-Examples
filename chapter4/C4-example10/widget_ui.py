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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(584, 455)
        icon = QIcon()
        icon.addFile(u":/icons/icons/aim.ico", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnInitItems = QPushButton(self.groupBox)
        self.btnInitItems.setObjectName(u"btnInitItems")

        self.gridLayout.addWidget(self.btnInitItems, 0, 0, 1, 1)

        self.chkEditable = QCheckBox(self.groupBox)
        self.chkEditable.setObjectName(u"chkEditable")

        self.gridLayout.addWidget(self.chkEditable, 0, 2, 1, 1)

        self.comboItems = QComboBox(self.groupBox)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/UNIT.ICO", QSize(), QIcon.Normal, QIcon.Off)
        self.comboItems.addItem(icon1, "")
        self.comboItems.addItem(icon1, "")
        self.comboItems.setObjectName(u"comboItems")

        self.gridLayout.addWidget(self.comboItems, 1, 0, 1, 3)

        self.btnClearItems = QPushButton(self.groupBox)
        self.btnClearItems.setObjectName(u"btnClearItems")

        self.gridLayout.addWidget(self.btnClearItems, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnInitCities = QPushButton(self.groupBox_3)
        self.btnInitCities.setObjectName(u"btnInitCities")

        self.verticalLayout.addWidget(self.btnInitCities)

        self.comboCities = QComboBox(self.groupBox_3)
        self.comboCities.setObjectName(u"comboCities")

        self.verticalLayout.addWidget(self.comboCities)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnClear = QPushButton(self.groupBox_2)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayout_2.addWidget(self.btnClear)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"ComboBoxDemo", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u7b80\u5355\u7684ComboBox", None))
        self.btnInitItems.setText(QCoreApplication.translate("Widget", u"\u521d\u59cb\u5316\u5217\u8868", None))
        self.chkEditable.setText(QCoreApplication.translate("Widget", u"\u53ef\u7f16\u8f91", None))
        self.comboItems.setItemText(0, QCoreApplication.translate("Widget", u"\u676d\u5dde", None))
        self.comboItems.setItemText(1, QCoreApplication.translate("Widget", u"\u5357\u660c", None))

        self.btnClearItems.setText(QCoreApplication.translate("Widget", u"\u6e05\u7a7a\u5217\u8868", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u6709\u7528\u6237\u6570\u636e\u7684ComboBox", None))
        self.btnInitCities.setText(QCoreApplication.translate("Widget", u"\u521d\u59cb\u5316\u57ce\u5e02+\u533a\u53f7", None))
        self.comboCities.setPlaceholderText(QCoreApplication.translate("Widget", u"\u8bf7\u9009\u62e9\u4e00\u4e2a\u57ce\u5e02", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.btnClear.setText(QCoreApplication.translate("Widget", u"\u6e05\u7a7a\u6587\u672c", None))
    # retranslateUi

