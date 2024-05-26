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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(686, 376)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.boyLabel = QLabel(Widget)
        self.boyLabel.setObjectName(u"boyLabel")

        self.gridLayout.addWidget(self.boyLabel, 0, 0, 1, 1)

        self.boySpinBox = QSpinBox(Widget)
        self.boySpinBox.setObjectName(u"boySpinBox")
        self.boySpinBox.setValue(10)

        self.gridLayout.addWidget(self.boySpinBox, 0, 1, 1, 1)

        self.boyPushButton = QPushButton(Widget)
        self.boyPushButton.setObjectName(u"boyPushButton")

        self.gridLayout.addWidget(self.boyPushButton, 0, 2, 1, 1)

        self.metaObjectInfoButton = QPushButton(Widget)
        self.metaObjectInfoButton.setObjectName(u"metaObjectInfoButton")

        self.gridLayout.addWidget(self.metaObjectInfoButton, 0, 3, 1, 1)

        self.girlLabel = QLabel(Widget)
        self.girlLabel.setObjectName(u"girlLabel")

        self.gridLayout.addWidget(self.girlLabel, 1, 0, 1, 1)

        self.girlSpinBox = QSpinBox(Widget)
        self.girlSpinBox.setObjectName(u"girlSpinBox")
        self.girlSpinBox.setValue(20)

        self.gridLayout.addWidget(self.girlSpinBox, 1, 1, 1, 1)

        self.girlPushButton = QPushButton(Widget)
        self.girlPushButton.setObjectName(u"girlPushButton")

        self.gridLayout.addWidget(self.girlPushButton, 1, 2, 1, 1)

        self.clearTextButton = QPushButton(Widget)
        self.clearTextButton.setObjectName(u"clearTextButton")

        self.gridLayout.addWidget(self.clearTextButton, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.plainTextEdit = QPlainTextEdit(Widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u5143\u7cfb\u7edfexample", None))
        self.boyLabel.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e\u7537\u751f\u5e74\u9f84", None))
        self.boyPushButton.setText(QCoreApplication.translate("Widget", u"\u7537\u751f\u957f\u5927\u4e00\u5c81", None))
        self.metaObjectInfoButton.setText(QCoreApplication.translate("Widget", u"\u5143\u5bf9\u8c61\u4fe1\u606f", None))
        self.girlLabel.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e\u5973\u751f\u5e74\u9f84", None))
        self.girlPushButton.setText(QCoreApplication.translate("Widget", u"\u5973\u751f\u957f\u5927\u4e00\u5c81", None))
        self.clearTextButton.setText(QCoreApplication.translate("Widget", u"\u6e05\u7a7a", None))
    # retranslateUi

