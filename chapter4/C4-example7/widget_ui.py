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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QProgressBar, QRadioButton, QScrollBar, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(589, 452)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dial = QDial(self.groupBox)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(200)
        self.dial.setValue(25)
        self.dial.setNotchesVisible(True)

        self.gridLayout.addWidget(self.dial, 0, 0, 2, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.groupBox)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setMaximum(200)
        self.horizontalScrollBar.setValue(25)
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalScrollBar, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setPageStep(25)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(200)
        self.progressBar.setValue(25)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.chkTextVisibility = QCheckBox(self.frame_2)
        self.chkTextVisibility.setObjectName(u"chkTextVisibility")

        self.gridLayout_2.addWidget(self.chkTextVisibility, 0, 0, 1, 1)

        self.chkInvertAppearance = QCheckBox(self.frame_2)
        self.chkInvertAppearance.setObjectName(u"chkInvertAppearance")

        self.gridLayout_2.addWidget(self.chkInvertAppearance, 0, 1, 1, 1)

        self.radioPercentage = QRadioButton(self.frame_2)
        self.radioPercentage.setObjectName(u"radioPercentage")

        self.gridLayout_2.addWidget(self.radioPercentage, 1, 0, 1, 1)

        self.radioCurrentValue = QRadioButton(self.frame_2)
        self.radioCurrentValue.setObjectName(u"radioCurrentValue")

        self.gridLayout_2.addWidget(self.radioCurrentValue, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u6ed1\u52a8\u8f93\u5165", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u6ed1\u52a8\u6761", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u5377\u6eda\u6761", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u8fdb\u5ea6\u6761\u663e\u793a\u548c\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u8fdb\u5ea6\u6761", None))
        self.progressBar.setFormat(QCoreApplication.translate("Widget", u"%p%", None))
        self.chkTextVisibility.setText(QCoreApplication.translate("Widget", u"testVisibility", None))
        self.chkInvertAppearance.setText(QCoreApplication.translate("Widget", u"invertAppearance", None))
        self.radioPercentage.setText(QCoreApplication.translate("Widget", u"\u663e\u793a\u683c\u5f0f\uff1a\u767e\u5206\u6bd4", None))
        self.radioCurrentValue.setText(QCoreApplication.translate("Widget", u"\u663e\u793a\u683c\u5f0f\uff1a\u5f53\u524d\u503c", None))
    # retranslateUi

