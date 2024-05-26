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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateEdit, QDateTimeEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTimeEdit,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(777, 322)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.groupBox)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(9, 0, 20)))
        self.timeEdit.setTimeSpec(Qt.LocalTime)
        self.timeEdit.setTime(QTime(9, 0, 20))

        self.gridLayout.addWidget(self.timeEdit, 1, 1, 1, 1)

        self.timeLineEdit = QLineEdit(self.groupBox)
        self.timeLineEdit.setObjectName(u"timeLineEdit")

        self.gridLayout.addWidget(self.timeLineEdit, 1, 2, 1, 1)

        self.qDebugTime = QPushButton(self.groupBox)
        self.qDebugTime.setObjectName(u"qDebugTime")

        self.gridLayout.addWidget(self.qDebugTime, 2, 1, 1, 1)

        self.btnSetTime = QPushButton(self.groupBox)
        self.btnSetTime.setObjectName(u"btnSetTime")

        self.gridLayout.addWidget(self.btnSetTime, 2, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 3, 1, 1, 1)

        self.dateLineEdit = QLineEdit(self.groupBox)
        self.dateLineEdit.setObjectName(u"dateLineEdit")

        self.gridLayout.addWidget(self.dateLineEdit, 3, 2, 1, 1)

        self.qDebugDate = QPushButton(self.groupBox)
        self.qDebugDate.setObjectName(u"qDebugDate")

        self.gridLayout.addWidget(self.qDebugDate, 4, 1, 1, 1)

        self.btnSetDate = QPushButton(self.groupBox)
        self.btnSetDate.setObjectName(u"btnSetDate")

        self.gridLayout.addWidget(self.btnSetDate, 4, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 5, 1, 1, 1)

        self.dateTimeLineEdit = QLineEdit(self.groupBox)
        self.dateTimeLineEdit.setObjectName(u"dateTimeLineEdit")

        self.gridLayout.addWidget(self.dateTimeLineEdit, 5, 2, 1, 1)

        self.qDebugDateTime = QPushButton(self.groupBox)
        self.qDebugDateTime.setObjectName(u"qDebugDateTime")

        self.gridLayout.addWidget(self.qDebugDateTime, 6, 1, 1, 1)

        self.btnSetDateTime = QPushButton(self.groupBox)
        self.btnSetDateTime.setObjectName(u"btnSetDateTime")

        self.gridLayout.addWidget(self.btnSetDateTime, 6, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.calendarWidget = QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_2.addWidget(self.calendarWidget, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u65e5\u671f\u548c\u65f6\u95f4", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u8bfb\u53d6\u5f53\u524d\u65e5\u671f\u65f6\u95f4", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u65f6\u95f4", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("Widget", u"HH:mm:ss", None))
        self.timeLineEdit.setInputMask(QCoreApplication.translate("Widget", u"99:99:99;_", None))
        self.qDebugTime.setText(QCoreApplication.translate("Widget", u"qDebug--Time", None))
        self.btnSetTime.setText(QCoreApplication.translate("Widget", u"fromString", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u65e5\u671f", None))
        self.dateLineEdit.setInputMask(QCoreApplication.translate("Widget", u"9999-99-99", None))
        self.qDebugDate.setText(QCoreApplication.translate("Widget", u"qDebug--Date", None))
        self.btnSetDate.setText(QCoreApplication.translate("Widget", u"fromString", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u65e5\u671f\u65f6\u95f4", None))
        self.dateTimeLineEdit.setInputMask(QCoreApplication.translate("Widget", u"9999-99-99 99:99:99", None))
        self.qDebugDateTime.setText(QCoreApplication.translate("Widget", u"qDebug--DateTime", None))
        self.btnSetDateTime.setText(QCoreApplication.translate("Widget", u"fromString", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5b57\u7b26\u4e32\u663e\u793a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u65e5\u5386\u9009\u62e9", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u7684\u65e5\u671f", None))
    # retranslateUi

