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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(438, 491)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAlignLeft = QPushButton(Widget)
        self.btnAlignLeft.setObjectName(u"btnAlignLeft")
        icon = QIcon()
        icon.addFile(u":/icons/images/508.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAlignLeft.setIcon(icon)
        self.btnAlignLeft.setCheckable(True)
        self.btnAlignLeft.setChecked(True)
        self.btnAlignLeft.setAutoExclusive(True)
        self.btnAlignLeft.setFlat(True)

        self.horizontalLayout.addWidget(self.btnAlignLeft)

        self.btnAlignCenter = QPushButton(Widget)
        self.btnAlignCenter.setObjectName(u"btnAlignCenter")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/510.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAlignCenter.setIcon(icon1)
        self.btnAlignCenter.setCheckable(True)
        self.btnAlignCenter.setAutoExclusive(True)
        self.btnAlignCenter.setFlat(True)

        self.horizontalLayout.addWidget(self.btnAlignCenter)

        self.btnAlignRight = QPushButton(Widget)
        self.btnAlignRight.setObjectName(u"btnAlignRight")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/512.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAlignRight.setIcon(icon2)
        self.btnAlignRight.setCheckable(True)
        self.btnAlignRight.setAutoExclusive(True)
        self.btnAlignRight.setFlat(True)

        self.horizontalLayout.addWidget(self.btnAlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnFontBold = QPushButton(Widget)
        self.btnFontBold.setObjectName(u"btnFontBold")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/500.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFontBold.setIcon(icon3)
        self.btnFontBold.setCheckable(True)
        self.btnFontBold.setChecked(True)
        self.btnFontBold.setAutoExclusive(False)
        self.btnFontBold.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnFontBold)

        self.btnFontItalic = QPushButton(Widget)
        self.btnFontItalic.setObjectName(u"btnFontItalic")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/502.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFontItalic.setIcon(icon4)
        self.btnFontItalic.setCheckable(True)
        self.btnFontItalic.setAutoExclusive(False)
        self.btnFontItalic.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnFontItalic)

        self.btnFontUnderline = QPushButton(Widget)
        self.btnFontUnderline.setObjectName(u"btnFontUnderline")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/504.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFontUnderline.setIcon(icon5)
        self.btnFontUnderline.setCheckable(True)
        self.btnFontUnderline.setAutoExclusive(False)
        self.btnFontUnderline.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnFontUnderline)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkReadOnly = QCheckBox(self.groupBox)
        self.checkReadOnly.setObjectName(u"checkReadOnly")

        self.horizontalLayout_3.addWidget(self.checkReadOnly)

        self.checkEnabled = QCheckBox(self.groupBox)
        self.checkEnabled.setObjectName(u"checkEnabled")
        self.checkEnabled.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkEnabled)

        self.checkClearEnabled = QCheckBox(self.groupBox)
        self.checkClearEnabled.setObjectName(u"checkClearEnabled")

        self.horizontalLayout_3.addWidget(self.checkClearEnabled)


        self.verticalLayout.addWidget(self.groupBox)

        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(True)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioBlack = QRadioButton(self.groupBox_2)
        self.radioBlack.setObjectName(u"radioBlack")

        self.horizontalLayout_5.addWidget(self.radioBlack)

        self.radioRed = QRadioButton(self.groupBox_2)
        self.radioRed.setObjectName(u"radioRed")

        self.horizontalLayout_5.addWidget(self.radioRed)

        self.radioBlue = QRadioButton(self.groupBox_2)
        self.radioBlue.setObjectName(u"radioBlue")

        self.horizontalLayout_5.addWidget(self.radioBlue)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(25)
        self.lineEdit.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btnAlignLeft.setText(QCoreApplication.translate("Widget", u"\u5c45\u5de6", None))
        self.btnAlignCenter.setText(QCoreApplication.translate("Widget", u"\u5c45\u4e2d", None))
        self.btnAlignRight.setText(QCoreApplication.translate("Widget", u"\u5c45\u53f3", None))
        self.btnFontBold.setText(QCoreApplication.translate("Widget", u"\u7c97\u4f53", None))
        self.btnFontItalic.setText(QCoreApplication.translate("Widget", u"\u659c\u4f53", None))
        self.btnFontUnderline.setText(QCoreApplication.translate("Widget", u"\u4e0b\u5212\u7ebf", None))
        self.groupBox.setTitle("")
        self.checkReadOnly.setText(QCoreApplication.translate("Widget", u"ReadOnly", None))
        self.checkEnabled.setText(QCoreApplication.translate("Widget", u"Enabled", None))
        self.checkClearEnabled.setText(QCoreApplication.translate("Widget", u"ClearButtonEnabled", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.radioBlack.setText(QCoreApplication.translate("Widget", u"Black", None))
        self.radioRed.setText(QCoreApplication.translate("Widget", u"Red", None))
        self.radioBlue.setText(QCoreApplication.translate("Widget", u"Blue", None))
        self.lineEdit.setText(QCoreApplication.translate("Widget", u"\u6d4b\u8bd5\u7528\u7684\u6587\u5b57", None))
    # retranslateUi

