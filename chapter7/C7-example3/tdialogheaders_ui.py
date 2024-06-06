# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdialogheaders.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_TDialogHeaders(object):
    def setupUi(self, TDialogHeaders):
        if not TDialogHeaders.objectName():
            TDialogHeaders.setObjectName(u"TDialogHeaders")
        TDialogHeaders.resize(398, 308)
        self.horizontalLayout = QHBoxLayout(TDialogHeaders)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(TDialogHeaders)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView = QListView(self.groupBox)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_2.addWidget(self.listView)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnOk = QPushButton(TDialogHeaders)
        self.btnOk.setObjectName(u"btnOk")
        icon = QIcon()
        icon.addFile(u":/images/images/704.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnOk.setIcon(icon)

        self.verticalLayout.addWidget(self.btnOk)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnCancel = QPushButton(TDialogHeaders)
        self.btnCancel.setObjectName(u"btnCancel")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/706.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCancel.setIcon(icon1)

        self.verticalLayout.addWidget(self.btnCancel)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(TDialogHeaders)
        self.btnOk.clicked.connect(TDialogHeaders.accept)
        self.btnCancel.clicked.connect(TDialogHeaders.reject)

        QMetaObject.connectSlotsByName(TDialogHeaders)
    # setupUi

    def retranslateUi(self, TDialogHeaders):
        TDialogHeaders.setWindowTitle(QCoreApplication.translate("TDialogHeaders", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("TDialogHeaders", u"\u8868\u5934\u6807\u9898", None))
        self.btnOk.setText(QCoreApplication.translate("TDialogHeaders", u"\u786e\u5b9a", None))
        self.btnCancel.setText(QCoreApplication.translate("TDialogHeaders", u"\u53d6\u6d88", None))
    # retranslateUi

