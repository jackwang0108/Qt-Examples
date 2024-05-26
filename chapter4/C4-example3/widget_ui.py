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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1020, 498)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(Widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnFrontBack = QPushButton(self.groupBox)
        self.btnFrontBack.setObjectName(u"btnFrontBack")

        self.gridLayout.addWidget(self.btnFrontBack, 0, 0, 1, 1)

        self.btnLeftRight = QPushButton(self.groupBox)
        self.btnLeftRight.setObjectName(u"btnLeftRight")

        self.gridLayout.addWidget(self.btnLeftRight, 0, 1, 1, 1)

        self.btnFirstLast = QPushButton(self.groupBox)
        self.btnFirstLast.setObjectName(u"btnFirstLast")

        self.gridLayout.addWidget(self.btnFirstLast, 1, 0, 1, 1)

        self.btnSection = QPushButton(self.groupBox)
        self.btnSection.setObjectName(u"btnSection")

        self.gridLayout.addWidget(self.btnSection, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnIsNullIsEmpty = QPushButton(self.groupBox_2)
        self.btnIsNullIsEmpty.setObjectName(u"btnIsNullIsEmpty")

        self.gridLayout_2.addWidget(self.btnIsNullIsEmpty, 0, 0, 1, 1)

        self.btnResize = QPushButton(self.groupBox_2)
        self.btnResize.setObjectName(u"btnResize")

        self.gridLayout_2.addWidget(self.btnResize, 0, 1, 1, 1)

        self.btnSizeLength = QPushButton(self.groupBox_2)
        self.btnSizeLength.setObjectName(u"btnSizeLength")

        self.gridLayout_2.addWidget(self.btnSizeLength, 1, 0, 1, 1)

        self.btnFill = QPushButton(self.groupBox_2)
        self.btnFill.setObjectName(u"btnFill")

        self.gridLayout_2.addWidget(self.btnFill, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnTrimmedSimplified = QPushButton(self.groupBox_3)
        self.btnTrimmedSimplified.setObjectName(u"btnTrimmedSimplified")

        self.gridLayout_3.addWidget(self.btnTrimmedSimplified, 0, 0, 1, 1)

        self.btnInsert = QPushButton(self.groupBox_3)
        self.btnInsert.setObjectName(u"btnInsert")

        self.gridLayout_3.addWidget(self.btnInsert, 0, 1, 1, 1)

        self.btnRemove = QPushButton(self.groupBox_3)
        self.btnRemove.setObjectName(u"btnRemove")

        self.gridLayout_3.addWidget(self.btnRemove, 1, 0, 1, 1)

        self.btnReplaced = QPushButton(self.groupBox_3)
        self.btnReplaced.setObjectName(u"btnReplaced")

        self.gridLayout_3.addWidget(self.btnReplaced, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBoxPath = QComboBox(self.groupBox_4)
        self.comboBoxPath.addItem("")
        self.comboBoxPath.addItem("")
        self.comboBoxPath.setObjectName(u"comboBoxPath")
        self.comboBoxPath.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.comboBoxPath)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.comboBoxDelim = QComboBox(self.groupBox_4)
        self.comboBoxDelim.addItem("")
        self.comboBoxDelim.addItem("")
        self.comboBoxDelim.addItem("")
        self.comboBoxDelim.setObjectName(u"comboBoxDelim")
        self.comboBoxDelim.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_4.addWidget(self.comboBoxDelim)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnClear = QPushButton(self.groupBox_5)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayout_3.addWidget(self.btnClear)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_3.addWidget(self.plainTextEdit)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.splitter.addWidget(self.frame_2)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"QString\u7279\u6027\u6d4b\u8bd5", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u5b57\u7b26\u4e32\u622a\u53d6", None))
        self.btnFrontBack.setText(QCoreApplication.translate("Widget", u"Front&&Back", None))
        self.btnLeftRight.setText(QCoreApplication.translate("Widget", u"Left&&Right", None))
        self.btnFirstLast.setText(QCoreApplication.translate("Widget", u"First&&Last", None))
        self.btnSection.setText(QCoreApplication.translate("Widget", u"Section*", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5b58\u50a8\u76f8\u5173", None))
        self.btnIsNullIsEmpty.setText(QCoreApplication.translate("Widget", u"isNull&&isEmpty", None))
        self.btnResize.setText(QCoreApplication.translate("Widget", u"resize", None))
        self.btnSizeLength.setText(QCoreApplication.translate("Widget", u"size&&length", None))
        self.btnFill.setText(QCoreApplication.translate("Widget", u"fill", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u8f6c\u6362\u6216\u4fee\u6539", None))
        self.btnTrimmedSimplified.setText(QCoreApplication.translate("Widget", u"trimmed&&simplified", None))
        self.btnInsert.setText(QCoreApplication.translate("Widget", u"insert", None))
        self.btnRemove.setText(QCoreApplication.translate("Widget", u"remove", None))
        self.btnReplaced.setText(QCoreApplication.translate("Widget", u"replace", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"\u8f93\u5165", None))
        self.label.setText(QCoreApplication.translate("Widget", u"path", None))
        self.comboBoxPath.setItemText(0, QCoreApplication.translate("Widget", u"/Users/jack/project/Qt6-Examples/chapter4/C4-exmaple3", None))
        self.comboBoxPath.setItemText(1, QCoreApplication.translate("Widget", u"        Are    you    OK    ?       ", None))

        self.label_2.setText(QCoreApplication.translate("Widget", u"delim", None))
        self.comboBoxDelim.setItemText(0, QCoreApplication.translate("Widget", u"/", None))
        self.comboBoxDelim.setItemText(1, QCoreApplication.translate("Widget", u"jack", None))
        self.comboBoxDelim.setItemText(2, QCoreApplication.translate("Widget", u":", None))

        self.label_3.setText(QCoreApplication.translate("Widget", u"\u53c2\u6570", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Widget", u"\u7ed3\u679c\u663e\u793a", None))
        self.btnClear.setText(QCoreApplication.translate("Widget", u"\u6e05\u7a7a\u6587\u672c\u6846", None))
    # retranslateUi

