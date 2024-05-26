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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(296, 377)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinNum = QSpinBox(self.groupBox)
        self.spinNum.setObjectName(u"spinNum")
        self.spinNum.setValue(4)

        self.gridLayout.addWidget(self.spinNum, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.spinPrice = QSpinBox(self.groupBox)
        self.spinPrice.setObjectName(u"spinPrice")
        self.spinPrice.setValue(12)

        self.gridLayout.addWidget(self.spinPrice, 0, 3, 1, 1)

        self.btnCalculate = QPushButton(self.groupBox)
        self.btnCalculate.setObjectName(u"btnCalculate")

        self.gridLayout.addWidget(self.btnCalculate, 1, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.spinTotal = QSpinBox(self.groupBox)
        self.spinTotal.setObjectName(u"spinTotal")
        self.spinTotal.setValue(99)

        self.gridLayout.addWidget(self.spinTotal, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.spinBin = QSpinBox(self.groupBox_2)
        self.spinBin.setObjectName(u"spinBin")
        self.spinBin.setDisplayIntegerBase(2)

        self.gridLayout_2.addWidget(self.spinBin, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.spinDec = QSpinBox(self.groupBox_2)
        self.spinDec.setObjectName(u"spinDec")

        self.gridLayout_2.addWidget(self.spinDec, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.spinHex = QSpinBox(self.groupBox_2)
        self.spinHex.setObjectName(u"spinHex")
        self.spinHex.setDisplayIntegerBase(16)

        self.gridLayout_2.addWidget(self.spinHex, 2, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u6570\u503c\u8f93\u5165\u8f93\u51fa", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u6570\u91cf", None))
        self.spinNum.setSuffix(QCoreApplication.translate("Widget", u" kg", None))
        self.spinNum.setPrefix("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u5355\u4ef7", None))
        self.spinPrice.setPrefix(QCoreApplication.translate("Widget", u"\uffe5", None))
        self.btnCalculate.setText(QCoreApplication.translate("Widget", u"\u8ba1\u7b97", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u603b\u4ef7", None))
        self.spinTotal.setPrefix(QCoreApplication.translate("Widget", u"\uffe5", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u8fdb\u5236\u8f6c\u6362", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u4e8c\u8fdb\u5236", None))
        self.spinBin.setPrefix(QCoreApplication.translate("Widget", u"BIN ", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5341\u8fdb\u5236", None))
        self.spinDec.setPrefix(QCoreApplication.translate("Widget", u"DEC ", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u5341\u516d\u8fdb\u5236", None))
        self.spinHex.setPrefix(QCoreApplication.translate("Widget", u"HEX ", None))
    # retranslateUi

