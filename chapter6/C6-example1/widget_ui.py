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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(701, 401)
        self.btnClick = QPushButton(Widget)
        self.btnClick.setObjectName(u"btnClick")
        self.btnClick.setGeometry(QRect(30, 20, 181, 171))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 217))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.btnClick.setPalette(palette)
        font = QFont()
        font.setBold(True)
        self.btnClick.setFont(font)
        self.btnClick.setFlat(False)
        self.labelClick = QLabel(Widget)
        self.labelClick.setObjectName(u"labelClick")
        self.labelClick.setGeometry(QRect(30, 280, 311, 101))
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 0, 0, 217))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        self.labelClick.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"3270 Nerd Font"])
        font1.setPointSize(24)
        font1.setBold(False)
        self.labelClick.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btnClick.setText(QCoreApplication.translate("Widget", u"Movable Button\n"
" \u6309WSAD\u79fb\u52a8", None))
        self.labelClick.setText(QCoreApplication.translate("Widget", u"\u70b9\u51fb\u9f20\u6807\u5de6\u952e", None))
    # retranslateUi

