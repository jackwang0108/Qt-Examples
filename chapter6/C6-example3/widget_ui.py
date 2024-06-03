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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(625, 374)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSingleClick = QLabel(Widget)
        self.labelSingleClick.setObjectName(u"labelSingleClick")
        font = QFont()
        font.setPointSize(19)
        self.labelSingleClick.setFont(font)
        self.labelSingleClick.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelSingleClick)

        self.labelDoubleClick = QLabel(Widget)
        self.labelDoubleClick.setObjectName(u"labelDoubleClick")
        self.labelDoubleClick.setFont(font)
        self.labelDoubleClick.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelDoubleClick)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.labelSingleClick.setText(QCoreApplication.translate("Widget", u"\u5355\u51fb\u6211", None))
        self.labelDoubleClick.setText(QCoreApplication.translate("Widget", u"\u53cc\u51fb\u6211", None))
    # retranslateUi

