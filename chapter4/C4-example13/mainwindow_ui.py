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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QScrollArea, QSizePolicy, QStatusBar, QToolBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actAddDir = QAction(MainWindow)
        self.actAddDir.setObjectName(u"actAddDir")
        icon = QIcon()
        icon.addFile(u":/images/icons/open3.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actAddDir.setIcon(icon)
        self.actAddDir.setMenuRole(QAction.NoRole)
        self.actAddFile = QAction(MainWindow)
        self.actAddFile.setObjectName(u"actAddFile")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/upfold1.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actAddFile.setIcon(icon1)
        self.actAddFile.setMenuRole(QAction.NoRole)
        self.actZoomIn = QAction(MainWindow)
        self.actZoomIn.setObjectName(u"actZoomIn")
        self.actZoomIn.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/418.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actZoomIn.setIcon(icon2)
        self.actZoomIn.setMenuRole(QAction.NoRole)
        self.actZoomOut = QAction(MainWindow)
        self.actZoomOut.setObjectName(u"actZoomOut")
        self.actZoomOut.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/416.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actZoomOut.setIcon(icon3)
        self.actZoomOut.setMenuRole(QAction.NoRole)
        self.actRealSize = QAction(MainWindow)
        self.actRealSize.setObjectName(u"actRealSize")
        self.actRealSize.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/414.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actRealSize.setIcon(icon4)
        self.actRealSize.setMenuRole(QAction.NoRole)
        self.actZoomFitWidth = QAction(MainWindow)
        self.actZoomFitWidth.setObjectName(u"actZoomFitWidth")
        self.actZoomFitWidth.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/424.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actZoomFitWidth.setIcon(icon5)
        self.actDeleteItem = QAction(MainWindow)
        self.actDeleteItem.setObjectName(u"actDeleteItem")
        self.actDeleteItem.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/images/icons/delete1.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actDeleteItem.setIcon(icon6)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        icon7 = QIcon()
        icon7.addFile(u":/images/icons/exit.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actQuit.setIcon(icon7)
        self.actZoomFitHeight = QAction(MainWindow)
        self.actZoomFitHeight.setObjectName(u"actZoomFitHeight")
        self.actZoomFitHeight.setEnabled(False)
        icon8 = QIcon()
        icon8.addFile(u":/images/icons/426.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actZoomFitHeight.setIcon(icon8)
        self.actScanItems = QAction(MainWindow)
        self.actScanItems.setObjectName(u"actScanItems")
        icon9 = QIcon()
        icon9.addFile(u":/images/icons/fold.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actScanItems.setIcon(icon9)
        self.actDockVisible = QAction(MainWindow)
        self.actDockVisible.setObjectName(u"actDockVisible")
        self.actDockVisible.setCheckable(True)
        self.actDockVisible.setChecked(True)
        icon10 = QIcon()
        icon10.addFile(u":/images/icons/BEBULB_16.ICO", QSize(), QIcon.Normal, QIcon.Off)
        self.actDockVisible.setIcon(icon10)
        self.actDockFloat = QAction(MainWindow)
        self.actDockFloat.setObjectName(u"actDockFloat")
        self.actDockFloat.setCheckable(True)
        self.actDockFloat.setChecked(False)
        icon11 = QIcon()
        icon11.addFile(u":/images/icons/814.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actDockFloat.setIcon(icon11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 486, 463))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelPic = QLabel(self.scrollAreaWidgetContents)
        self.labelPic.setObjectName(u"labelPic")
        self.labelPic.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPic, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeWidget = QTreeWidget(self.dockWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        icon12 = QIcon()
        icon12.addFile(u":/images/icons/15.ico", QSize(), QIcon.Normal, QIcon.Off)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setIcon(2, icon12);
        QTreeWidgetItem(__qtreewidgetitem1)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout.addWidget(self.treeWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actAddDir)
        self.menu.addAction(self.actAddFile)
        self.menu.addAction(self.actScanItems)
        self.menu.addAction(self.actDeleteItem)
        self.menu.addSeparator()
        self.menu.addAction(self.actQuit)
        self.menu_2.addAction(self.actZoomIn)
        self.menu_2.addAction(self.actZoomOut)
        self.menu_2.addAction(self.actRealSize)
        self.menu_2.addAction(self.actZoomFitWidth)
        self.mainToolBar.addAction(self.actAddDir)
        self.mainToolBar.addAction(self.actAddFile)
        self.mainToolBar.addAction(self.actDeleteItem)
        self.mainToolBar.addAction(self.actScanItems)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actZoomIn)
        self.mainToolBar.addAction(self.actZoomOut)
        self.mainToolBar.addAction(self.actRealSize)
        self.mainToolBar.addAction(self.actZoomFitHeight)
        self.mainToolBar.addAction(self.actZoomFitWidth)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actDockFloat)
        self.mainToolBar.addAction(self.actDockVisible)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actAddDir.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.actAddDir.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u76ee\u5f55...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actAddDir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actAddFile.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.actAddFile.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actAddFile.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actZoomIn.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5927", None))
#if QT_CONFIG(tooltip)
        self.actZoomIn.setToolTip(QCoreApplication.translate("MainWindow", u"\u653e\u5927", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actZoomIn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actZoomOut.setText(QCoreApplication.translate("MainWindow", u"\u7f29\u5c0f", None))
#if QT_CONFIG(tooltip)
        self.actZoomOut.setToolTip(QCoreApplication.translate("MainWindow", u"\u7f29\u5c0f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actZoomOut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actRealSize.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u9645\u5927\u5c0f", None))
#if QT_CONFIG(tooltip)
        self.actRealSize.setToolTip(QCoreApplication.translate("MainWindow", u"\u5b9e\u9645\u5927\u5c0f", None))
#endif // QT_CONFIG(tooltip)
        self.actZoomFitWidth.setText(QCoreApplication.translate("MainWindow", u"\u9002\u5408\u5bbd\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.actZoomFitWidth.setToolTip(QCoreApplication.translate("MainWindow", u"\u9002\u5408\u5bbd\u5ea6\u663e\u793a\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actZoomFitWidth.setStatusTip(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bbd\u5ea6\u9002\u5e94\u663e\u793a\u533a\u5bbd\u5ea6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actZoomFitWidth.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actDeleteItem.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u8282\u70b9", None))
#if QT_CONFIG(tooltip)
        self.actDeleteItem.setToolTip(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u8282\u70b9", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actDeleteItem.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5f53\u524d\u8282\u70b9", None))
#endif // QT_CONFIG(statustip)
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actQuit.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u672c\u7cfb\u7edf", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actQuit.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u672c\u7cfb\u7edf", None))
#endif // QT_CONFIG(statustip)
        self.actZoomFitHeight.setText(QCoreApplication.translate("MainWindow", u"\u9002\u5408\u9ad8\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.actZoomFitHeight.setToolTip(QCoreApplication.translate("MainWindow", u"\u9002\u5408\u9ad8\u5ea6\u663e\u793a\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actZoomFitHeight.setStatusTip(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u9ad8\u5ea6\u9002\u5e94\u663e\u793a\u533a\u9ad8\u5ea6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actZoomFitHeight.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actScanItems.setText(QCoreApplication.translate("MainWindow", u"\u904d\u5386\u8282\u70b9", None))
#if QT_CONFIG(tooltip)
        self.actScanItems.setToolTip(QCoreApplication.translate("MainWindow", u"\u904d\u5386\u8282\u70b9", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actScanItems.setStatusTip(QCoreApplication.translate("MainWindow", u"\u904d\u5386\u6240\u6709\u8282\u70b9\uff0c\u8282\u70b9\u6807\u9898\u524d\u52a0*", None))
#endif // QT_CONFIG(statustip)
        self.actDockVisible.setText(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u53ef\u89c1", None))
#if QT_CONFIG(tooltip)
        self.actDockVisible.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u9760\u7a97\u53e3\u53ef\u89c1", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actDockVisible.setStatusTip(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6216\u9690\u85cf\u56fe\u7247\u76ee\u5f55\u6811", None))
#endif // QT_CONFIG(statustip)
        self.actDockFloat.setText(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u6d6e\u52a8", None))
#if QT_CONFIG(tooltip)
        self.actDockFloat.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u9760\u7a97\u53e3\u6d6e\u52a8", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actDockFloat.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4f7f\u56fe\u7247\u76ee\u5f55\u6811\u7a97\u53e3\u6d6e\u52a8\u663e\u793a", None))
#endif // QT_CONFIG(statustip)
        self.labelPic.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8981\u663e\u793a\u7684\u56fe\u7247", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u76ee\u5f55\u6811", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.mainToolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u8282\u70b9\u7c7b\u578b", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u8282\u70b9", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u6587\u4ef6", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5b50\u9879\u76ee", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

