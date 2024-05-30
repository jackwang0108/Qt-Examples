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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QSizePolicy,
    QSpacerItem, QSplitter, QToolBar, QToolBox,
    QToolButton, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 632)
        self.actListInit = QAction(MainWindow)
        self.actListInit.setObjectName(u"actListInit")
        icon = QIcon()
        icon.addFile(u":/images/icons/128.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actListInit.setIcon(icon)
        self.actListInit.setMenuRole(QAction.NoRole)
        self.actListClear = QAction(MainWindow)
        self.actListClear.setObjectName(u"actListClear")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/delete1.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actListClear.setIcon(icon1)
        self.actListClear.setMenuRole(QAction.NoRole)
        self.actListInsert = QAction(MainWindow)
        self.actListInsert.setObjectName(u"actListInsert")
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/424.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actListInsert.setIcon(icon2)
        self.actListInsert.setMenuRole(QAction.NoRole)
        self.actListAppend = QAction(MainWindow)
        self.actListAppend.setObjectName(u"actListAppend")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/316.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actListAppend.setIcon(icon3)
        self.actListAppend.setMenuRole(QAction.NoRole)
        self.actListRemove = QAction(MainWindow)
        self.actListRemove.setObjectName(u"actListRemove")
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/324.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actListRemove.setIcon(icon4)
        self.actListRemove.setMenuRole(QAction.NoRole)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/exit.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actQuit.setIcon(icon5)
        self.actQuit.setMenuRole(QAction.NoRole)
        self.actSelAll = QAction(MainWindow)
        self.actSelAll.setObjectName(u"actSelAll")
        self.actSelAll.setMenuRole(QAction.NoRole)
        self.actSelNone = QAction(MainWindow)
        self.actSelNone.setObjectName(u"actSelNone")
        self.actSelNone.setMenuRole(QAction.NoRole)
        self.actSelInv = QAction(MainWindow)
        self.actSelInv.setObjectName(u"actSelInv")
        self.actSelInv.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.toolBox = QToolBox(self.splitter)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(700, 16777215))
        font = QFont()
        font.setFamilies([u"3270 Nerd Font"])
        font.setPointSize(14)
        self.toolBox.setFont(font)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 304, 434))
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tBtnListInit = QToolButton(self.page)
        self.tBtnListInit.setObjectName(u"tBtnListInit")
        self.tBtnListInit.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tBtnListInit.setAutoRaise(True)

        self.gridLayout.addWidget(self.tBtnListInit, 0, 0, 1, 1)

        self.tBtnListClear = QToolButton(self.page)
        self.tBtnListClear.setObjectName(u"tBtnListClear")
        self.tBtnListClear.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tBtnListClear.setAutoRaise(True)

        self.gridLayout.addWidget(self.tBtnListClear, 1, 0, 1, 1)

        self.tBtnListInsert = QToolButton(self.page)
        self.tBtnListInsert.setObjectName(u"tBtnListInsert")
        self.tBtnListInsert.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tBtnListInsert.setAutoRaise(True)

        self.gridLayout.addWidget(self.tBtnListInsert, 2, 0, 1, 1)

        self.tBtnListAppend = QToolButton(self.page)
        self.tBtnListAppend.setObjectName(u"tBtnListAppend")
        self.tBtnListAppend.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tBtnListAppend.setAutoRaise(True)

        self.gridLayout.addWidget(self.tBtnListAppend, 3, 0, 1, 1)

        self.tBtnListDelete = QToolButton(self.page)
        self.tBtnListDelete.setObjectName(u"tBtnListDelete")
        self.tBtnListDelete.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tBtnListDelete.setAutoRaise(True)

        self.gridLayout.addWidget(self.tBtnListDelete, 4, 0, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u":/images/icons/410.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon6, u"\u5217\u8868\u9879\u64cd\u4f5c")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 304, 434))
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.chkSortEnable = QCheckBox(self.page_2)
        self.chkSortEnable.setObjectName(u"chkSortEnable")
        font1 = QFont()
        font1.setFamilies([u"3270 Nerd Font"])
        font1.setPointSize(24)
        self.chkSortEnable.setFont(font1)

        self.gridLayout_2.addWidget(self.chkSortEnable, 0, 0, 1, 1)

        self.tBtnSortAsc = QToolButton(self.page_2)
        self.tBtnSortAsc.setObjectName(u"tBtnSortAsc")
        self.tBtnSortAsc.setFont(font1)
        self.tBtnSortAsc.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tBtnSortAsc.setArrowType(Qt.UpArrow)

        self.gridLayout_2.addWidget(self.tBtnSortAsc, 1, 0, 1, 1)

        self.tBtnSortDes = QToolButton(self.page_2)
        self.tBtnSortDes.setObjectName(u"tBtnSortDes")
        self.tBtnSortDes.setFont(font1)
        self.tBtnSortDes.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tBtnSortDes.setArrowType(Qt.DownArrow)

        self.gridLayout_2.addWidget(self.tBtnSortDes, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 228, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)

        icon7 = QIcon()
        icon7.addFile(u":/images/icons/408.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon7, u"\u5217\u8868\u6392\u5e8f")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 304, 434))
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tBtnTextClear = QToolButton(self.page_3)
        self.tBtnTextClear.setObjectName(u"tBtnTextClear")

        self.gridLayout_3.addWidget(self.tBtnTextClear, 0, 0, 1, 1)

        self.tBtnTextAddLine = QToolButton(self.page_3)
        self.tBtnTextAddLine.setObjectName(u"tBtnTextAddLine")

        self.gridLayout_3.addWidget(self.tBtnTextAddLine, 0, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.page_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_3.addWidget(self.plainTextEdit, 1, 0, 1, 2)

        icon8 = QIcon()
        icon8.addFile(u":/images/icons/412.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon8, u"\u4fe1\u53f7\u53d1\u5c04\u65f6\u673a")
        self.splitter.addWidget(self.toolBox)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.editCurrentItemText = QLineEdit(self.groupBox)
        self.editCurrentItemText.setObjectName(u"editCurrentItemText")

        self.horizontalLayout.addWidget(self.editCurrentItemText)

        self.chkListEditable = QCheckBox(self.groupBox)
        self.chkListEditable.setObjectName(u"chkListEditable")
        self.chkListEditable.setChecked(True)

        self.horizontalLayout.addWidget(self.chkListEditable)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tBtnSelItem = QToolButton(self.groupBox)
        self.tBtnSelItem.setObjectName(u"tBtnSelItem")
        self.tBtnSelItem.setPopupMode(QToolButton.MenuButtonPopup)

        self.horizontalLayout_2.addWidget(self.tBtnSelItem)

        self.tBtnSelAll = QToolButton(self.groupBox)
        self.tBtnSelAll.setObjectName(u"tBtnSelAll")

        self.horizontalLayout_2.addWidget(self.tBtnSelAll)

        self.tBtnSelNone = QToolButton(self.groupBox)
        self.tBtnSelNone.setObjectName(u"tBtnSelNone")

        self.horizontalLayout_2.addWidget(self.tBtnSelNone)

        self.tBtnSelInv = QToolButton(self.groupBox)
        self.tBtnSelInv.setObjectName(u"tBtnSelInv")

        self.horizontalLayout_2.addWidget(self.tBtnSelInv)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.listWidget = QListWidget(self.groupBox)
        icon9 = QIcon()
        icon9.addFile(u":/images/icons/check2.ico", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem.setIcon(icon9);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setCheckState(Qt.Checked);
        __qlistwidgetitem1.setIcon(icon9);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout.addWidget(self.listWidget)

        self.splitter.addWidget(self.groupBox)

        self.horizontalLayout_3.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actListInit)
        self.toolBar.addAction(self.actListClear)
        self.toolBar.addAction(self.actListInsert)
        self.toolBar.addAction(self.actListAppend)
        self.toolBar.addAction(self.actListRemove)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actListInit.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.actListInit.setToolTip(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actListInit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actListClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.actListClear.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
        self.actListInsert.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u5165\u9879", None))
#if QT_CONFIG(tooltip)
        self.actListInsert.setToolTip(QCoreApplication.translate("MainWindow", u"\u63d2\u5165\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actListInsert.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actListAppend.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u9879", None))
#if QT_CONFIG(tooltip)
        self.actListAppend.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actListAppend.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actListRemove.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5f53\u524d\u9879", None))
#if QT_CONFIG(tooltip)
        self.actListRemove.setToolTip(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5f53\u524d\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actQuit.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.actSelAll.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
#if QT_CONFIG(tooltip)
        self.actSelAll.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5168\u90e8\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
        self.actSelNone.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u9009\u62e9", None))
#if QT_CONFIG(tooltip)
        self.actSelNone.setToolTip(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u9009\u62e9\u7684\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
        self.actSelInv.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u9009\u62e9", None))
#if QT_CONFIG(tooltip)
        self.actSelInv.setToolTip(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u9009\u62e9\u5f53\u524d\u7684\u5217\u8868\u9879", None))
#endif // QT_CONFIG(tooltip)
        self.tBtnListInit.setText(QCoreApplication.translate("MainWindow", u"tBtnListInit", None))
        self.tBtnListClear.setText(QCoreApplication.translate("MainWindow", u"tBtnListClear", None))
        self.tBtnListInsert.setText(QCoreApplication.translate("MainWindow", u"tBtnListInsert", None))
        self.tBtnListAppend.setText(QCoreApplication.translate("MainWindow", u"tBtnListAppend", None))
        self.tBtnListDelete.setText(QCoreApplication.translate("MainWindow", u"tBtnListDelete", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u5217\u8868\u9879\u64cd\u4f5c", None))
        self.chkSortEnable.setText(QCoreApplication.translate("MainWindow", u"\u5141\u8bb8\u6392\u5e8f", None))
        self.tBtnSortAsc.setText(QCoreApplication.translate("MainWindow", u"\u5347\u5e8f\u6392\u5e8f", None))
        self.tBtnSortDes.setText(QCoreApplication.translate("MainWindow", u"\u964d\u5e8f\u6392\u5e8f", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u5217\u8868\u6392\u5e8f", None))
        self.tBtnTextClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6587\u672c", None))
        self.tBtnTextAddLine.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7a7a\u884c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u4fe1\u53f7\u53d1\u5c04\u65f6\u673a", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u9879\u53d8\u5316", None))
        self.chkListEditable.setText(QCoreApplication.translate("MainWindow", u"\u9879\u53ef\u7f16\u8f91", None))
        self.tBtnSelItem.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u9009\u9879", None))
        self.tBtnSelAll.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u9009\u62e9", None))
        self.tBtnSelNone.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u9009\u62e9", None))
        self.tBtnSelInv.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u9009\u62e9", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee2", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

