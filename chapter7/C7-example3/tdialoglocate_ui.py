# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdialoglocate.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
import res_rc

class Ui_TDialogLocate(object):
    def setupUi(self, TDialogLocate):
        if not TDialogLocate.objectName():
            TDialogLocate.setObjectName(u"TDialogLocate")
        TDialogLocate.resize(438, 151)
        self.horizontalLayout = QHBoxLayout(TDialogLocate)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(TDialogLocate)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinRow = QSpinBox(self.groupBox)
        self.spinRow.setObjectName(u"spinRow")

        self.gridLayout.addWidget(self.spinRow, 0, 1, 1, 1)

        self.chkRowInc = QCheckBox(self.groupBox)
        self.chkRowInc.setObjectName(u"chkRowInc")

        self.gridLayout.addWidget(self.chkRowInc, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinCol = QSpinBox(self.groupBox)
        self.spinCol.setObjectName(u"spinCol")

        self.gridLayout.addWidget(self.spinCol, 1, 1, 1, 1)

        self.chkColInc = QCheckBox(self.groupBox)
        self.chkColInc.setObjectName(u"chkColInc")

        self.gridLayout.addWidget(self.chkColInc, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnOk = QPushButton(TDialogLocate)
        self.btnOk.setObjectName(u"btnOk")
        icon = QIcon()
        icon.addFile(u":/images/images/506.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnOk.setIcon(icon)

        self.verticalLayout.addWidget(self.btnOk)

        self.btnCancel = QPushButton(TDialogLocate)
        self.btnCancel.setObjectName(u"btnCancel")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/132.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCancel.setIcon(icon1)

        self.verticalLayout.addWidget(self.btnCancel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(TDialogLocate)
        self.btnCancel.clicked.connect(TDialogLocate.close)

        QMetaObject.connectSlotsByName(TDialogLocate)
    # setupUi

    def retranslateUi(self, TDialogLocate):
        TDialogLocate.setWindowTitle(QCoreApplication.translate("TDialogLocate", u"Dialog", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("TDialogLocate", u"\u884c\u53f7", None))
        self.chkRowInc.setText(QCoreApplication.translate("TDialogLocate", u"\u884c\u589e", None))
        self.label_2.setText(QCoreApplication.translate("TDialogLocate", u"\u5217\u53f7", None))
        self.chkColInc.setText(QCoreApplication.translate("TDialogLocate", u"\u5217\u589e", None))
        self.label_3.setText(QCoreApplication.translate("TDialogLocate", u"\u6587\u5b57", None))
        self.btnOk.setText(QCoreApplication.translate("TDialogLocate", u"\u8bbe\u7f6e\u6587\u5b57", None))
        self.btnCancel.setText(QCoreApplication.translate("TDialogLocate", u"\u5173\u95ed", None))
    # retranslateUi

