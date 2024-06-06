# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdialogsize.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_TDialogSize(object):
    def setupUi(self, TDialogSize):
        if not TDialogSize.objectName():
            TDialogSize.setObjectName(u"TDialogSize")
        TDialogSize.resize(332, 112)
        self.horizontalLayout = QHBoxLayout(TDialogSize)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(TDialogSize)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinColNum = QSpinBox(self.groupBox)
        self.spinColNum.setObjectName(u"spinColNum")

        self.gridLayout.addWidget(self.spinColNum, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinRowNum = QSpinBox(self.groupBox)
        self.spinRowNum.setObjectName(u"spinRowNum")

        self.gridLayout.addWidget(self.spinRowNum, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnOk = QPushButton(TDialogSize)
        self.btnOk.setObjectName(u"btnOk")

        self.verticalLayout.addWidget(self.btnOk)

        self.btnCancel = QPushButton(TDialogSize)
        self.btnCancel.setObjectName(u"btnCancel")

        self.verticalLayout.addWidget(self.btnCancel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(TDialogSize)
        self.btnOk.clicked.connect(TDialogSize.accept)
        self.btnCancel.clicked.connect(TDialogSize.reject)

        QMetaObject.connectSlotsByName(TDialogSize)
    # setupUi

    def retranslateUi(self, TDialogSize):
        TDialogSize.setWindowTitle(QCoreApplication.translate("TDialogSize", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("TDialogSize", u"\u8868\u683c\u7684\u884c\u5217\u6570", None))
        self.label.setText(QCoreApplication.translate("TDialogSize", u"\u5217\u6570", None))
        self.label_2.setText(QCoreApplication.translate("TDialogSize", u"\u884c\u6570", None))
        self.btnOk.setText(QCoreApplication.translate("TDialogSize", u"\u786e\u8ba4", None))
        self.btnCancel.setText(QCoreApplication.translate("TDialogSize", u"\u53d6\u6d88", None))
    # retranslateUi

