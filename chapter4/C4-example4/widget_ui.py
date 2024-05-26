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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(414, 388)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.editNum = QLineEdit(self.groupBox)
        self.editNum.setObjectName(u"editNum")

        self.gridLayout.addWidget(self.editNum, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.editPrice = QLineEdit(self.groupBox)
        self.editPrice.setObjectName(u"editPrice")

        self.gridLayout.addWidget(self.editPrice, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.editTotal = QLineEdit(self.groupBox)
        self.editTotal.setObjectName(u"editTotal")

        self.gridLayout.addWidget(self.editTotal, 1, 3, 1, 1)

        self.btnTotal = QPushButton(self.groupBox)
        self.btnTotal.setObjectName(u"btnTotal")

        self.gridLayout.addWidget(self.btnTotal, 2, 1, 1, 1)

        self.btnCalTotal = QPushButton(self.groupBox)
        self.btnCalTotal.setObjectName(u"btnCalTotal")

        self.gridLayout.addWidget(self.btnCalTotal, 2, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.editDecimal = QLineEdit(self.groupBox_2)
        self.editDecimal.setObjectName(u"editDecimal")

        self.gridLayout_2.addWidget(self.editDecimal, 0, 1, 1, 1)

        self.btnDec = QPushButton(self.groupBox_2)
        self.btnDec.setObjectName(u"btnDec")

        self.gridLayout_2.addWidget(self.btnDec, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.editBinary = QLineEdit(self.groupBox_2)
        self.editBinary.setObjectName(u"editBinary")

        self.gridLayout_2.addWidget(self.editBinary, 1, 1, 1, 1)

        self.btnBin = QPushButton(self.groupBox_2)
        self.btnBin.setObjectName(u"btnBin")

        self.gridLayout_2.addWidget(self.btnBin, 1, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.editHex = QLineEdit(self.groupBox_2)
        self.editHex.setObjectName(u"editHex")

        self.gridLayout_2.addWidget(self.editHex, 2, 1, 1, 1)

        self.btnHex = QPushButton(self.groupBox_2)
        self.btnHex.setObjectName(u"btnHex")

        self.gridLayout_2.addWidget(self.btnHex, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u6570\u503c\u8f93\u5165\u548c\u8f93\u51fa", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u6570\u91cf", None))
        self.editNum.setText(QCoreApplication.translate("Widget", u"12", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u5355\u4ef7", None))
        self.editPrice.setText(QCoreApplication.translate("Widget", u"5.5", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u603b\u4ef7", None))
        self.btnTotal.setText(QCoreApplication.translate("Widget", u"qDebug()\u6d4b\u8bd5", None))
        self.btnCalTotal.setText(QCoreApplication.translate("Widget", u"\u8ba1\u7b97\u603b\u4ef7", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u8fdb\u5236\u8f6c\u6362", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u5341\u8fdb\u5236", None))
        self.btnDec.setText(QCoreApplication.translate("Widget", u"DEC ---> \u5176\u4ed6\u8fdb\u5236", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u4e8c\u8fdb\u5236", None))
        self.btnBin.setText(QCoreApplication.translate("Widget", u"BIN ---> \u5176\u4ed6\u8fdb\u5236", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u5341\u516d\u8fdb\u5236", None))
        self.btnHex.setText(QCoreApplication.translate("Widget", u"HEX ---> \u5176\u4ed6\u8fdb\u5236", None))
    # retranslateUi

