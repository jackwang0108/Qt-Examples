# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tformdoc.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPlainTextEdit, QSizePolicy,
    QWidget)

class Ui_TFormDoc(object):
    def setupUi(self, TFormDoc):
        if not TFormDoc.objectName():
            TFormDoc.setObjectName(u"TFormDoc")
        TFormDoc.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(TFormDoc)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(TFormDoc)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)


        self.retranslateUi(TFormDoc)

        QMetaObject.connectSlotsByName(TFormDoc)
    # setupUi

    def retranslateUi(self, TFormDoc):
        TFormDoc.setWindowTitle(QCoreApplication.translate("TFormDoc", u"Form", None))
    # retranslateUi

