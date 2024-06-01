# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QListView, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSplitter, QTableView,
    QToolBar, QTreeView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actSetRootFolder = QAction(MainWindow)
        self.actSetRootFolder.setObjectName(u"actSetRootFolder")
        icon = QIcon()
        icon.addFile(u":/images/icons/folder1.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actSetRootFolder.setIcon(icon)
        self.actSetRootFolder.setMenuRole(QAction.NoRole)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/exit.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actQuit.setIcon(icon1)
        self.actQuit.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitterMain = QSplitter(self.centralwidget)
        self.splitterMain.setObjectName(u"splitterMain")
        self.splitterMain.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitterMain)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioFolderFile = QRadioButton(self.frame)
        self.radioFolderFile.setObjectName(u"radioFolderFile")

        self.horizontalLayout.addWidget(self.radioFolderFile)

        self.radioFolderOnly = QRadioButton(self.frame)
        self.radioFolderOnly.setObjectName(u"radioFolderOnly")

        self.horizontalLayout.addWidget(self.radioFolderOnly)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.groupFilter = QGroupBox(self.frame)
        self.groupFilter.setObjectName(u"groupFilter")
        self.horizontalLayout_2 = QHBoxLayout(self.groupFilter)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chkEnableFilter = QCheckBox(self.groupFilter)
        self.chkEnableFilter.setObjectName(u"chkEnableFilter")

        self.horizontalLayout_2.addWidget(self.chkEnableFilter)

        self.comboFilter = QComboBox(self.groupFilter)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")
        self.comboFilter.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.comboFilter)

        self.btnApplyFilter = QPushButton(self.groupFilter)
        self.btnApplyFilter.setObjectName(u"btnApplyFilter")
        self.btnApplyFilter.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/828.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.btnApplyFilter.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btnApplyFilter)

        self.horizontalSpacer_2 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.groupFilter)


        self.verticalLayout_4.addWidget(self.frame)

        self.treeView = QTreeView(self.groupBox)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_4.addWidget(self.treeView)

        self.splitterMain.addWidget(self.groupBox)
        self.splitter = QSplitter(self.splitterMain)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listView = QListView(self.groupBox_2)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.splitter.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.groupBox_3)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.splitter.addWidget(self.groupBox_3)
        self.splitterMain.addWidget(self.splitter)

        self.verticalLayout_5.addWidget(self.splitterMain)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelFileName = QLabel(self.centralwidget)
        self.labelFileName.setObjectName(u"labelFileName")

        self.horizontalLayout_3.addWidget(self.labelFileName)

        self.labelFileSize = QLabel(self.centralwidget)
        self.labelFileSize.setObjectName(u"labelFileSize")

        self.horizontalLayout_3.addWidget(self.labelFileSize)

        self.labelNodeType = QLabel(self.centralwidget)
        self.labelNodeType.setObjectName(u"labelNodeType")

        self.horizontalLayout_3.addWidget(self.labelNodeType)

        self.chkIsDir = QCheckBox(self.centralwidget)
        self.chkIsDir.setObjectName(u"chkIsDir")

        self.horizontalLayout_3.addWidget(self.chkIsDir)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.labelFilePath = QLabel(self.centralwidget)
        self.labelFilePath.setObjectName(u"labelFilePath")

        self.verticalLayout_5.addWidget(self.labelFilePath)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actSetRootFolder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u76ee\u5f55\u6811Demo", None))
        self.actSetRootFolder.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6839\u76ee\u5f55", None))
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"TreeView", None))
        self.radioFolderFile.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u76ee\u5f55\u548c\u6587\u4ef6", None))
        self.radioFolderOnly.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u76ee\u5f55", None))
        self.groupFilter.setTitle("")
        self.chkEnableFilter.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8fc7\u6ee4", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"*.h;*.cpp;*.ui", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"*.txt", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"*.jpg", None))

        self.btnApplyFilter.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"ListView", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"TableView", None))
        self.labelFileName.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.labelFileSize.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5927\u5c0f", None))
        self.labelNodeType.setText(QCoreApplication.translate("MainWindow", u"\u8282\u70b9\u7c7b\u578b", None))
        self.chkIsDir.setText(QCoreApplication.translate("MainWindow", u"\u8282\u70b9\u662f\u5426\u662f\u76ee\u5f55", None))
        self.labelFilePath.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u540d", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

