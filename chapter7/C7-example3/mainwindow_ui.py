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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
    QTabWidget, QToolBar, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actWindowInSide = QAction(MainWindow)
        self.actWindowInSide.setObjectName(u"actWindowInSide")
        icon = QIcon()
        icon.addFile(u":/images/images/2.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actWindowInSide.setIcon(icon)
        self.actWindowInSide.setMenuRole(QAction.NoRole)
        self.actWidgetInSide = QAction(MainWindow)
        self.actWidgetInSide.setObjectName(u"actWidgetInSide")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/100.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actWidgetInSide.setIcon(icon1)
        self.actWidgetInSide.setMenuRole(QAction.NoRole)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/132.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actQuit.setIcon(icon2)
        self.actQuit.setMenuRole(QAction.NoRole)
        self.actWindow = QAction(MainWindow)
        self.actWindow.setObjectName(u"actWindow")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actWindow.setIcon(icon3)
        self.actWindow.setMenuRole(QAction.NoRole)
        self.actWidget = QAction(MainWindow)
        self.actWidget.setObjectName(u"actWidget")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/804.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actWidget.setIcon(icon4)
        self.actWidget.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(120, 140, 521, 241))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actWindowInSide)
        self.toolBar.addAction(self.actWidgetInSide)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actWindow)
        self.toolBar.addAction(self.actWidget)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actWindowInSide.setText(QCoreApplication.translate("MainWindow", u"\u5d4c\u5165\u5f0fMainWindow", None))
#if QT_CONFIG(tooltip)
        self.actWindowInSide.setToolTip(QCoreApplication.translate("MainWindow", u"\u5d4c\u5165\u5f0fMainWindow", None))
#endif // QT_CONFIG(tooltip)
        self.actWidgetInSide.setText(QCoreApplication.translate("MainWindow", u"\u5d4c\u5165\u5f0fWidget", None))
#if QT_CONFIG(tooltip)
        self.actWidgetInSide.setToolTip(QCoreApplication.translate("MainWindow", u"\u5d4c\u5165\u5f0fWidget", None))
#endif // QT_CONFIG(tooltip)
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actWindow.setText(QCoreApplication.translate("MainWindow", u"\u72ec\u7acb\u7684MainWindow", None))
#if QT_CONFIG(tooltip)
        self.actWindow.setToolTip(QCoreApplication.translate("MainWindow", u"\u72ec\u7acb\u7684MainWindow", None))
#endif // QT_CONFIG(tooltip)
        self.actWidget.setText(QCoreApplication.translate("MainWindow", u"\u72ec\u7acb\u7684Widget", None))
#if QT_CONFIG(tooltip)
        self.actWidget.setToolTip(QCoreApplication.translate("MainWindow", u"\u72ec\u7acb\u7684Widget", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

