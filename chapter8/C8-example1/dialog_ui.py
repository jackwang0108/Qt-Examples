# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSplitter,
    QToolBox, QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(927, 616)
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(Dialog)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.toolBox = QToolBox(self.splitter)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(400, 16777215))
        self.toolBox.setFrameShape(QFrame.StyledPanel)
        self.pageApp = QWidget()
        self.pageApp.setObjectName(u"pageApp")
        self.pageApp.setGeometry(QRect(0, 0, 349, 352))
        self.verticalLayout_3 = QVBoxLayout(self.pageApp)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_8 = QGroupBox(self.pageApp)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.groupBox_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_62 = QPushButton(self.groupBox_8)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.pushButton_62)

        self.pushButton_4 = QPushButton(self.groupBox_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_61 = QPushButton(self.groupBox_8)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.pushButton_61)

        self.pushButton_40 = QPushButton(self.groupBox_8)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.pushButton_40)


        self.verticalLayout_3.addWidget(self.groupBox_8)

        icon = QIcon()
        icon.addFile(u":/images/images/802.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.pageApp, icon, u"QCoreApplication\u7c7b")
        self.pageFile = QWidget()
        self.pageFile.setObjectName(u"pageFile")
        self.pageFile.setGeometry(QRect(0, 0, 349, 352))
        self.verticalLayout_8 = QVBoxLayout(self.pageFile)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_10 = QGroupBox(self.pageFile)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_7 = QGridLayout(self.groupBox_10)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_48 = QPushButton(self.groupBox_10)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(0, 25))

        self.gridLayout_7.addWidget(self.pushButton_48, 0, 0, 1, 1)

        self.pushButton_49 = QPushButton(self.groupBox_10)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(0, 25))

        self.gridLayout_7.addWidget(self.pushButton_49, 1, 0, 1, 1)

        self.pushButton_50 = QPushButton(self.groupBox_10)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(0, 25))

        self.gridLayout_7.addWidget(self.pushButton_50, 1, 1, 1, 1)

        self.pushButton_51 = QPushButton(self.groupBox_10)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMinimumSize(QSize(0, 25))

        self.gridLayout_7.addWidget(self.pushButton_51, 0, 1, 1, 1)

        self.pushButton_63 = QPushButton(self.groupBox_10)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setMinimumSize(QSize(0, 25))

        self.gridLayout_7.addWidget(self.pushButton_63, 2, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.pageFile)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_5 = QGridLayout(self.groupBox_9)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_53 = QPushButton(self.groupBox_9)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(0, 25))

        self.gridLayout_5.addWidget(self.pushButton_53, 0, 0, 1, 1)

        self.pushButton_56 = QPushButton(self.groupBox_9)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMinimumSize(QSize(0, 25))

        self.gridLayout_5.addWidget(self.pushButton_56, 2, 1, 1, 1)

        self.pushButton_55 = QPushButton(self.groupBox_9)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setMinimumSize(QSize(0, 25))

        self.gridLayout_5.addWidget(self.pushButton_55, 2, 0, 1, 1)

        self.pushButton_54 = QPushButton(self.groupBox_9)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setMinimumSize(QSize(0, 25))

        self.gridLayout_5.addWidget(self.pushButton_54, 0, 1, 1, 1)

        self.pushButton_64 = QPushButton(self.groupBox_9)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setMinimumSize(QSize(0, 25))

        self.gridLayout_5.addWidget(self.pushButton_64, 3, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_9)

        icon1 = QIcon()
        icon1.addFile(u":/images/images/804.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.pageFile, icon1, u"QFile\u7c7b")
        self.pageFileInfo = QWidget()
        self.pageFileInfo.setObjectName(u"pageFileInfo")
        self.pageFileInfo.setGeometry(QRect(0, 0, 349, 352))
        self.verticalLayout_5 = QVBoxLayout(self.pageFileInfo)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.groupBox_6 = QGroupBox(self.pageFileInfo)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.pushButton_30 = QPushButton(self.groupBox_6)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_30, 3, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.groupBox_6)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_29, 0, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.groupBox_6)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_28, 0, 0, 1, 1)

        self.pushButton_31 = QPushButton(self.groupBox_6)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_31, 3, 1, 1, 1)

        self.pushButton_42 = QPushButton(self.groupBox_6)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_42, 6, 0, 1, 1)

        self.pushButton_43 = QPushButton(self.groupBox_6)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_43, 6, 1, 1, 1)

        self.pushButton_35 = QPushButton(self.groupBox_6)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_35, 7, 0, 1, 1)

        self.pushButton_36 = QPushButton(self.groupBox_6)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_36, 8, 0, 1, 1)

        self.pushButton_44 = QPushButton(self.groupBox_6)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_44, 8, 1, 1, 1)

        self.pushButton_33 = QPushButton(self.groupBox_6)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_33, 1, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.groupBox_6)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_27, 10, 1, 1, 1)

        self.pushButton_39 = QPushButton(self.groupBox_6)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_39, 4, 0, 1, 1)

        self.pushButton_59 = QPushButton(self.groupBox_6)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_59, 10, 0, 1, 1)

        self.pushButton_32 = QPushButton(self.groupBox_6)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_32, 4, 1, 1, 1)

        self.pushButton_34 = QPushButton(self.groupBox_6)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_34, 1, 1, 1, 1)

        self.pushButton_37 = QPushButton(self.groupBox_6)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_37, 2, 1, 1, 1)

        self.pushButton_38 = QPushButton(self.groupBox_6)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_38, 2, 0, 1, 1)

        self.pushButton_58 = QPushButton(self.groupBox_6)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pushButton_58, 7, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_6)

        icon2 = QIcon()
        icon2.addFile(u":/images/images/135.JPG", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.pageFileInfo, icon2, u"QFileInfo\u7c7b")
        self.pageDir = QWidget()
        self.pageDir.setObjectName(u"pageDir")
        self.pageDir.setGeometry(QRect(0, -68, 334, 420))
        self.verticalLayout_4 = QVBoxLayout(self.pageDir)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.pageDir)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 25))

        self.gridLayout_3.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 25))

        self.gridLayout_3.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 25))

        self.gridLayout_3.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 25))

        self.gridLayout_3.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 25))

        self.gridLayout_3.addWidget(self.pushButton_6, 2, 0, 1, 1)

        self.pushButton_60 = QPushButton(self.groupBox)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setMinimumSize(QSize(0, 25))

        self.gridLayout_3.addWidget(self.pushButton_60, 2, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.pageDir)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_20 = QPushButton(self.groupBox_4)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.pushButton_20, 0, 0, 1, 1)

        self.pushButton_22 = QPushButton(self.groupBox_4)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.pushButton_22, 2, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.groupBox_4)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.pushButton_23, 2, 1, 1, 1)

        self.pushButton_26 = QPushButton(self.groupBox_4)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.pushButton_26, 3, 0, 1, 1)

        self.pushButton_24 = QPushButton(self.groupBox_4)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.pushButton_24, 0, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.pageDir)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_19 = QPushButton(self.groupBox_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_19, 1, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_11, 4, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.groupBox_3)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_17, 4, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.groupBox_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_14, 0, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_15, 1, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.groupBox_3)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_18, 3, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_13, 0, 0, 1, 1)

        self.pushButton_65 = QPushButton(self.groupBox_3)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_65, 2, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.groupBox_3)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_16, 2, 1, 1, 1)

        self.pushButton_66 = QPushButton(self.groupBox_3)
        self.pushButton_66.setObjectName(u"pushButton_66")

        self.gridLayout.addWidget(self.pushButton_66, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        icon3 = QIcon()
        icon3.addFile(u":/images/images/007.GIF", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.pageDir, icon3, u"QDir\u7c7b")
        self.pageTempDir = QWidget()
        self.pageTempDir.setObjectName(u"pageTempDir")
        self.pageTempDir.setGeometry(QRect(0, 0, 349, 352))
        self.horizontalLayout_2 = QHBoxLayout(self.pageTempDir)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_5 = QGroupBox(self.pageTempDir)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_21 = QPushButton(self.groupBox_5)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 25))

        self.verticalLayout_7.addWidget(self.pushButton_21)

        self.pushButton_67 = QPushButton(self.groupBox_5)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMinimumSize(QSize(0, 25))

        self.verticalLayout_7.addWidget(self.pushButton_67)

        self.pushButton_68 = QPushButton(self.groupBox_5)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMinimumSize(QSize(0, 25))

        self.verticalLayout_7.addWidget(self.pushButton_68)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        icon4 = QIcon()
        icon4.addFile(u":/images/images/806.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.pageTempDir, icon4, u"QTemporaryDir\u7c7b")
        self.pageTempFile = QWidget()
        self.pageTempFile.setObjectName(u"pageTempFile")
        self.pageTempFile.setGeometry(QRect(0, 0, 349, 352))
        self.verticalLayout_11 = QVBoxLayout(self.pageTempFile)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_12 = QGroupBox(self.pageTempFile)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_25 = QPushButton(self.groupBox_12)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(0, 25))

        self.verticalLayout_12.addWidget(self.pushButton_25)

        self.pushButton_69 = QPushButton(self.groupBox_12)
        self.pushButton_69.setObjectName(u"pushButton_69")

        self.verticalLayout_12.addWidget(self.pushButton_69)

        self.pushButton_70 = QPushButton(self.groupBox_12)
        self.pushButton_70.setObjectName(u"pushButton_70")

        self.verticalLayout_12.addWidget(self.pushButton_70)


        self.verticalLayout_11.addWidget(self.groupBox_12)

        icon5 = QIcon()
        icon5.addFile(u":/images/images/174.JPG", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.pageTempFile, icon5, u"QTemporaryFile\u7c7b")
        self.pageWatcher = QWidget()
        self.pageWatcher.setObjectName(u"pageWatcher")
        self.pageWatcher.setGeometry(QRect(0, 0, 349, 352))
        self.verticalLayout_9 = QVBoxLayout(self.pageWatcher)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_11 = QGroupBox(self.pageWatcher)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_46 = QPushButton(self.groupBox_11)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(0, 25))

        self.verticalLayout_6.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.groupBox_11)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(0, 25))

        self.verticalLayout_6.addWidget(self.pushButton_47)

        self.pushButton_52 = QPushButton(self.groupBox_11)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMinimumSize(QSize(0, 25))

        self.verticalLayout_6.addWidget(self.pushButton_52)

        self.pushButton_57 = QPushButton(self.groupBox_11)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setMinimumSize(QSize(0, 25))

        self.verticalLayout_6.addWidget(self.pushButton_57)


        self.verticalLayout_9.addWidget(self.groupBox_11)

        icon6 = QIcon()
        icon6.addFile(u":/images/images/714.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.pageWatcher, icon6, u"QFileSystemWatcher\u7c7b")
        self.splitter.addWidget(self.toolBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_41 = QPushButton(self.groupBox_7)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(0, 30))
        self.pushButton_41.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_41)

        self.pushButton_45 = QPushButton(self.groupBox_7)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(0, 30))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/122.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_45.setIcon(icon7)

        self.horizontalLayout.addWidget(self.pushButton_45)

        self.pushButton_5 = QPushButton(self.groupBox_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 30))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/212.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon8)

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.editFile = QLineEdit(self.groupBox_2)
        self.editFile.setObjectName(u"editFile")
        self.editFile.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.editFile, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.editDir = QLineEdit(self.groupBox_2)
        self.editDir.setObjectName(u"editDir")
        self.editDir.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.editDir, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.gridLayout_6.addWidget(self.plainTextEdit, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)

        self.splitter.addWidget(self.groupBox_2)

        self.verticalLayout_10.addWidget(self.splitter)


        self.retranslateUi(Dialog)

        self.toolBox.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u76ee\u5f55\u548c\u6587\u4ef6\u64cd\u4f5c", None))
        self.groupBox_8.setTitle("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Dialog", u"Returns the directory that contains the application executable", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"applicationDirPath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Dialog", u"Returns the file path of the application executable", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"applicationFilePath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("Dialog", u"This property holds the name of this application", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"applicationName()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_62.setToolTip(QCoreApplication.translate("Dialog", u"set the name of this application", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_62.setText(QCoreApplication.translate("Dialog", u"setApplicationName()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("Dialog", u"Returns a list of paths that the application will search when dynamically loading libraries", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"libraryPaths()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_61.setToolTip(QCoreApplication.translate("Dialog", u"This property holds the name of the organization that wrote this application", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_61.setText(QCoreApplication.translate("Dialog", u"organizationName()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_40.setToolTip(QCoreApplication.translate("Dialog", u"Tells the application to exit with a return code.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_40.setText(QCoreApplication.translate("Dialog", u"exit() \u9000\u51fa\u5e94\u7528\u7a0b\u5e8f", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageApp), QCoreApplication.translate("Dialog", u"QCoreApplication\u7c7b", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Dialog", u"\u9759\u6001\u51fd\u6570", None))
#if QT_CONFIG(tooltip)
        self.pushButton_48.setToolTip(QCoreApplication.translate("Dialog", u"Copies the file fileName to newName.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_48.setText(QCoreApplication.translate("Dialog", u"copy()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_49.setToolTip(QCoreApplication.translate("Dialog", u"Removes the file specified by the fileName given.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_49.setText(QCoreApplication.translate("Dialog", u"remove()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_50.setToolTip(QCoreApplication.translate("Dialog", u"Renames the file oldName to newName. ", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_50.setText(QCoreApplication.translate("Dialog", u"rename()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_51.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if the file specified by fileName exists; otherwise returns false.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_51.setText(QCoreApplication.translate("Dialog", u"exists()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_63.setToolTip(QCoreApplication.translate("Dialog", u"Moves a specific file to the trash", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_63.setText(QCoreApplication.translate("Dialog", u"moveToTrash()", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog", u"\u6210\u5458\u51fd\u6570", None))
#if QT_CONFIG(tooltip)
        self.pushButton_53.setToolTip(QCoreApplication.translate("Dialog", u"Copies the file currently specified by fileName() to a file called newName", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_53.setText(QCoreApplication.translate("Dialog", u"copy()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_56.setToolTip(QCoreApplication.translate("Dialog", u"Renames the file currently specified by fileName() to newName. Returns true if successful; otherwise returns false.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_56.setText(QCoreApplication.translate("Dialog", u"rename()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_55.setToolTip(QCoreApplication.translate("Dialog", u"Removes the file specified by fileName(). Returns true if successful; otherwise returns false.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_55.setText(QCoreApplication.translate("Dialog", u"remove()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_54.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if the file specified by fileName() exists; otherwise returns false.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_54.setText(QCoreApplication.translate("Dialog", u"exists()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_64.setToolTip(QCoreApplication.translate("Dialog", u"Moves the file specified by fileName() to the trash", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_64.setText(QCoreApplication.translate("Dialog", u"moveToTrash()", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageFile), QCoreApplication.translate("Dialog", u"QFile\u7c7b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.pushButton_30.setToolTip(QCoreApplication.translate("Dialog", u"The base name consists of all characters in the file up to (but not including) the first '.' character", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_30.setText(QCoreApplication.translate("Dialog", u"baseName()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_29.setToolTip(QCoreApplication.translate("Dialog", u"Returns a file's path absolute path. This doesn't include the file name", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_29.setText(QCoreApplication.translate("Dialog", u"absolutePath() ", None))
#if QT_CONFIG(tooltip)
        self.pushButton_28.setToolTip(QCoreApplication.translate("Dialog", u"Returns an absolute path including the file name", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_28.setText(QCoreApplication.translate("Dialog", u"absoluteFilePath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_31.setToolTip(QCoreApplication.translate("Dialog", u"The complete base name consists of all characters in the file up to (but not including) the last '.' character", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_31.setText(QCoreApplication.translate("Dialog", u"completeBaseName()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_42.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if this object points to a directory or to a symbolic link to a directory; otherwise returns false", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_42.setText(QCoreApplication.translate("Dialog", u"isDir()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_43.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if this object points to a file or to a symbolic link to a file", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_43.setText(QCoreApplication.translate("Dialog", u"isFile()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_35.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if the file is executable; otherwise returns false.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_35.setText(QCoreApplication.translate("Dialog", u"isExecutable()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_36.setToolTip(QCoreApplication.translate("Dialog", u"Returns the date and time when the file was last modified.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_36.setText(QCoreApplication.translate("Dialog", u"lastModified()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_44.setToolTip(QCoreApplication.translate("Dialog", u"Returns the date and time when the file was last read (accessed).", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_44.setText(QCoreApplication.translate("Dialog", u"lastRead()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_33.setToolTip(QCoreApplication.translate("Dialog", u"Returns the name of the file, excluding the path.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_33.setText(QCoreApplication.translate("Dialog", u"fileName()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_27.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if the file exists; otherwise returns false", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_27.setText(QCoreApplication.translate("Dialog", u"exists()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_39.setToolTip(QCoreApplication.translate("Dialog", u"The suffix consists of all characters in the file after (but not including) the last '.'", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_39.setText(QCoreApplication.translate("Dialog", u"suffix()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_59.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if the file exists; otherwise returns false", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_59.setText(QCoreApplication.translate("Dialog", u"\u9759\u6001\u51fd\u6570exists()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_32.setToolTip(QCoreApplication.translate("Dialog", u"The complete suffix consists of all characters in the file after (but not including) the first '.'", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_32.setText(QCoreApplication.translate("Dialog", u"completeSuffix()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_34.setToolTip(QCoreApplication.translate("Dialog", u"Returns the file name, including the path (which may be absolute or relative).", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_34.setText(QCoreApplication.translate("Dialog", u"filePath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_37.setToolTip(QCoreApplication.translate("Dialog", u"Returns the file's path. This doesn't include the file name.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_37.setText(QCoreApplication.translate("Dialog", u"path()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_38.setToolTip(QCoreApplication.translate("Dialog", u"Returns the file size in bytes.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_38.setText(QCoreApplication.translate("Dialog", u"size()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_58.setToolTip(QCoreApplication.translate("Dialog", u"Returns the date and time when the file was created", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_58.setText(QCoreApplication.translate("Dialog", u"birthTime()", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageFileInfo), QCoreApplication.translate("Dialog", u"QFileInfo\u7c7b", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u9759\u6001\u51fd\u6570", None))
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("Dialog", u"Returns the absolute path of the user's home directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"homePath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(QCoreApplication.translate("Dialog", u"Returns the absolute canonical path of the system's temporary directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"tempPath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("Dialog", u"Returns the absolute path of the root directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"rootPath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("Dialog", u"Returns a list of the root directories on this system", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"drives()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("Dialog", u"Returns the absolute path of the application's current directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"currentPath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_60.setToolTip(QCoreApplication.translate("Dialog", u"Sets the application's current working directory to path", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_60.setText(QCoreApplication.translate("Dialog", u"setCurrent()", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u6216\u76ee\u5f55\u64cd\u4f5c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_20.setToolTip(QCoreApplication.translate("Dialog", u"Creates a sub-directory called dirName.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_20.setText(QCoreApplication.translate("Dialog", u"mkdir()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_22.setToolTip(QCoreApplication.translate("Dialog", u"Removes the file, fileName.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_22.setText(QCoreApplication.translate("Dialog", u"remove()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_23.setToolTip(QCoreApplication.translate("Dialog", u"Renames a file or directory from oldName to newName", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_23.setText(QCoreApplication.translate("Dialog", u"rename()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_26.setToolTip(QCoreApplication.translate("Dialog", u"Sets the path of the directory to path", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_26.setText(QCoreApplication.translate("Dialog", u"setPath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_24.setToolTip(QCoreApplication.translate("Dialog", u"Removes the directory specified by dirName.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_24.setText(QCoreApplication.translate("Dialog", u"rmdir()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(QCoreApplication.translate("Dialog", u"Removes the directory, including all its contents.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setText(QCoreApplication.translate("Dialog", u"removeRecursively()", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u6216\u76ee\u5f55\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.pushButton_19.setToolTip(QCoreApplication.translate("Dialog", u"Returns the path name of a file in the directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_19.setText(QCoreApplication.translate("Dialog", u"filePath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(QCoreApplication.translate("Dialog", u"Returns a list of the names of all the files and directories in the directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"entryList(dir)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_17.setToolTip(QCoreApplication.translate("Dialog", u"Returns a list of the names of all the files and directories in the directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_17.setText(QCoreApplication.translate("Dialog", u"entryList(file)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_14.setToolTip(QCoreApplication.translate("Dialog", u"Returns the absolute path (a path that starts with \"/\" or with a drive specification)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_14.setText(QCoreApplication.translate("Dialog", u"absolutePath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_15.setToolTip(QCoreApplication.translate("Dialog", u"Returns the canonical path, i.e. a path without symbolic links or redundant \".\" or \"..\" elements.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_15.setText(QCoreApplication.translate("Dialog", u"canonicalPath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_18.setToolTip(QCoreApplication.translate("Dialog", u"Returns true if the directory exists", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_18.setText(QCoreApplication.translate("Dialog", u"exists()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_13.setToolTip(QCoreApplication.translate("Dialog", u"Returns the absolute path name of a file in the directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_13.setText(QCoreApplication.translate("Dialog", u"absoluteFilePath()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_65.setToolTip(QCoreApplication.translate("Dialog", u"Returns the path", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_65.setText(QCoreApplication.translate("Dialog", u"path()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_16.setToolTip(QCoreApplication.translate("Dialog", u"Returns the name of the directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_16.setText(QCoreApplication.translate("Dialog", u"dirName()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_66.setToolTip(QCoreApplication.translate("Dialog", u"Returns whether the directory is empty", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_66.setText(QCoreApplication.translate("Dialog", u"isEmpty()", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageDir), QCoreApplication.translate("Dialog", u"QDir\u7c7b", None))
#if QT_CONFIG(tooltip)
        self.groupBox_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_5.setTitle("")
#if QT_CONFIG(tooltip)
        self.pushButton_21.setToolTip(QCoreApplication.translate("Dialog", u"\u5728QDir::tempPath()\u8fd4\u56de\u7684\u7cfb\u7edf\u4e34\u65f6\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_21.setText(QCoreApplication.translate("Dialog", u"1.\u5728\u7cfb\u7edf\u4e34\u65f6\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.pushButton_67.setToolTip(QCoreApplication.translate("Dialog", u"\u5728\u6307\u5b9a\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_67.setText(QCoreApplication.translate("Dialog", u"2.\u5728\u6307\u5b9a\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.pushButton_68.setToolTip(QCoreApplication.translate("Dialog", u"\u5728QDir::currentPath()\u8868\u793a\u7684\u5f53\u524d\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_68.setText(QCoreApplication.translate("Dialog", u"3.\u5728\u5f53\u524d\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6\u5939", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageTempDir), QCoreApplication.translate("Dialog", u"QTemporaryDir\u7c7b", None))
        self.groupBox_12.setTitle("")
#if QT_CONFIG(tooltip)
        self.pushButton_25.setToolTip(QCoreApplication.translate("Dialog", u"\u5728QDir::tempPath()\u8fd4\u56de\u7684\u7cfb\u7edf\u4e34\u65f6\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_25.setText(QCoreApplication.translate("Dialog", u"1. \u5728\u7cfb\u7edf\u4e34\u65f6\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.pushButton_69.setToolTip(QCoreApplication.translate("Dialog", u"\u5728\u6307\u5b9a\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_69.setText(QCoreApplication.translate("Dialog", u"2.\u5728\u6307\u5b9a\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.pushButton_70.setToolTip(QCoreApplication.translate("Dialog", u"\u5728QDir::currentPath()\u8868\u793a\u7684\u5f53\u524d\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_70.setText(QCoreApplication.translate("Dialog", u"3.\u5728\u5f53\u524d\u76ee\u5f55\u4e0b\u521b\u5efa\u4e34\u65f6\u6587\u4ef6", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageTempFile), QCoreApplication.translate("Dialog", u"QTemporaryFile\u7c7b", None))
        self.groupBox_11.setTitle("")
#if QT_CONFIG(tooltip)
        self.pushButton_46.setToolTip(QCoreApplication.translate("Dialog", u"Adds path to the file system watcher if path exists.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_46.setText(QCoreApplication.translate("Dialog", u"addPath()\u5e76\u5f00\u59cb\u76d1\u89c6", None))
#if QT_CONFIG(tooltip)
        self.pushButton_47.setToolTip(QCoreApplication.translate("Dialog", u"Removes the specified path from the file system watcher.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_47.setText(QCoreApplication.translate("Dialog", u"removePath()\u5e76\u505c\u6b62\u76d1\u89c6", None))
#if QT_CONFIG(tooltip)
        self.pushButton_52.setToolTip(QCoreApplication.translate("Dialog", u"Returns a list of paths to directories that are being watched.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_52.setText(QCoreApplication.translate("Dialog", u"directories()", None))
#if QT_CONFIG(tooltip)
        self.pushButton_57.setToolTip(QCoreApplication.translate("Dialog", u"Returns a list of paths to files that are being watched.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_57.setText(QCoreApplication.translate("Dialog", u"files()", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageWatcher), QCoreApplication.translate("Dialog", u"QFileSystemWatcher\u7c7b", None))
        self.groupBox_2.setTitle("")
        self.groupBox_7.setTitle("")
        self.pushButton_41.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u6587\u4ef6", None))
        self.pushButton_45.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u76ee\u5f55", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u6e05\u9664\u6587\u672c\u6846", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6587 \u4ef6 ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u76ee \u5f55 ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u4fe1 \u606f ", None))
    # retranslateUi

