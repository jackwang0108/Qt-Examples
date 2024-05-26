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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(553, 462)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnStart = QPushButton(self.groupBox)
        self.btnStart.setObjectName(u"btnStart")

        self.gridLayout.addWidget(self.btnStart, 0, 0, 1, 1)

        self.btnStop = QPushButton(self.groupBox)
        self.btnStop.setObjectName(u"btnStop")

        self.gridLayout.addWidget(self.btnStop, 0, 1, 1, 1)

        self.btnDynamic = QPushButton(self.groupBox)
        self.btnDynamic.setObjectName(u"btnDynamic")

        self.gridLayout.addWidget(self.btnDynamic, 0, 2, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(999999)
        self.spinBox.setValue(2000)

        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)

        self.radioOnce = QRadioButton(self.groupBox)
        self.radioOnce.setObjectName(u"radioOnce")

        self.gridLayout.addWidget(self.radioOnce, 1, 2, 1, 1)

        self.radioMulti = QRadioButton(self.groupBox)
        self.radioMulti.setObjectName(u"radioMulti")
        self.radioMulti.setChecked(True)

        self.gridLayout.addWidget(self.radioMulti, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnPrecise = QRadioButton(self.groupBox_2)
        self.btnPrecise.setObjectName(u"btnPrecise")

        self.horizontalLayout.addWidget(self.btnPrecise)

        self.btnCoarse = QRadioButton(self.groupBox_2)
        self.btnCoarse.setObjectName(u"btnCoarse")
        self.btnCoarse.setChecked(True)

        self.horizontalLayout.addWidget(self.btnCoarse)

        self.btnVeryCoarse = QRadioButton(self.groupBox_2)
        self.btnVeryCoarse.setObjectName(u"btnVeryCoarse")

        self.horizontalLayout.addWidget(self.btnVeryCoarse)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lcdHour = QLCDNumber(self.groupBox_3)
        self.lcdHour.setObjectName(u"lcdHour")
        self.lcdHour.setDigitCount(2)
        self.lcdHour.setProperty("value", 23.000000000000000)

        self.horizontalLayout_2.addWidget(self.lcdHour)

        self.lcdMin = QLCDNumber(self.groupBox_3)
        self.lcdMin.setObjectName(u"lcdMin")
        self.lcdMin.setDigitCount(2)
        self.lcdMin.setProperty("value", 23.000000000000000)

        self.horizontalLayout_2.addWidget(self.lcdMin)

        self.lcdSec = QLCDNumber(self.groupBox_3)
        self.lcdSec.setObjectName(u"lcdSec")
        self.lcdSec.setDigitCount(2)
        self.lcdSec.setProperty("value", 23.000000000000000)

        self.horizontalLayout_2.addWidget(self.lcdSec)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.labelElapsed = QLabel(Widget)
        self.labelElapsed.setObjectName(u"labelElapsed")

        self.verticalLayout.addWidget(self.labelElapsed)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u5b9a\u65f6\u5668", None))
        self.btnStart.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb", None))
        self.btnStop.setText(QCoreApplication.translate("Widget", u"\u505c\u6b62", None))
        self.btnDynamic.setText(QCoreApplication.translate("Widget", u"\u52a8\u6001\u521b\u5efa\u5355\u6b21\u5b9a\u65f6\u5668", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u5b9a\u65f6\u5468\u671f", None))
        self.spinBox.setSuffix(QCoreApplication.translate("Widget", u" ms", None))
        self.radioOnce.setText(QCoreApplication.translate("Widget", u"\u5355\u6b21\u8ba1\u65f6", None))
        self.radioMulti.setText(QCoreApplication.translate("Widget", u"\u8fde\u7eed\u8ba1\u65f6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5b9a\u65f6\u5668\u7cbe\u5ea6", None))
        self.btnPrecise.setText(QCoreApplication.translate("Widget", u"PreciseTimer", None))
        self.btnCoarse.setText(QCoreApplication.translate("Widget", u"CoarseTimer", None))
        self.btnVeryCoarse.setText(QCoreApplication.translate("Widget", u"VeryCoarseTimer", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u5f53\u524d\u65f6\u95f4\uff08\u65f6:\u5206:\u79d2\uff09", None))
        self.labelElapsed.setText(QCoreApplication.translate("Widget", u"\u6d41\u901d\u7684\u65f6\u95f4", None))
    # retranslateUi

