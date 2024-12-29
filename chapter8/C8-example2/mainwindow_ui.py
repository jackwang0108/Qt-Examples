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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit, QSizePolicy,
    QStatusBar, QTabWidget, QToolBar, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(693, 450)
        font = QFont()
        font.setFamilies([u"Hiragino Sans GB"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actOpen_IODevice = QAction(MainWindow)
        self.actOpen_IODevice.setObjectName(u"actOpen_IODevice")
        icon = QIcon()
        icon.addFile(u":/images/images/804.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actOpen_IODevice.setIcon(icon)
        self.actOpen_TextStream = QAction(MainWindow)
        self.actOpen_TextStream.setObjectName(u"actOpen_TextStream")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/122.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actOpen_TextStream.setIcon(icon1)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/132.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actQuit.setIcon(icon2)
        self.actSave_IODevice = QAction(MainWindow)
        self.actSave_IODevice.setObjectName(u"actSave_IODevice")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/104.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actSave_IODevice.setIcon(icon3)
        self.actSave_TextStream = QAction(MainWindow)
        self.actSave_TextStream.setObjectName(u"actSave_TextStream")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/floppy.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actSave_TextStream.setIcon(icon4)
        self.actSave_TextSafe = QAction(MainWindow)
        self.actSave_TextSafe.setObjectName(u"actSave_TextSafe")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/066.GIF", QSize(), QIcon.Normal, QIcon.Off)
        self.actSave_TextSafe.setIcon(icon5)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 10, 651, 371))
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.textEditDevice = QPlainTextEdit(self.tab)
        self.textEditDevice.setObjectName(u"textEditDevice")
        font1 = QFont()
        font1.setFamilies([u"Hiragino Sans GB"])
        font1.setPointSize(11)
        self.textEditDevice.setFont(font1)

        self.verticalLayout.addWidget(self.textEditDevice)

        icon6 = QIcon()
        icon6.addFile(u":/images/images/29.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.textEditStream = QPlainTextEdit(self.tab_2)
        self.textEditStream.setObjectName(u"textEditStream")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 0, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush3 = QBrush(QColor(0, 0, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        brush5 = QBrush(QColor(0, 0, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEditStream.setPalette(palette)
        self.textEditStream.setFont(font1)

        self.verticalLayout_2.addWidget(self.textEditStream)

        icon7 = QIcon()
        icon7.addFile(u":/images/images/133.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon7, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.mainToolBar.addAction(self.actOpen_IODevice)
        self.mainToolBar.addAction(self.actSave_IODevice)
        self.mainToolBar.addAction(self.actSave_TextSafe)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actOpen_TextStream)
        self.mainToolBar.addAction(self.actSave_TextStream)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u6587\u4ef6\u8bfb\u5199", None))
        self.actOpen_IODevice.setText(QCoreApplication.translate("MainWindow", u"QFile\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.actOpen_IODevice.setToolTip(QCoreApplication.translate("MainWindow", u"\u7528QFile\u6253\u5f00\u6587\u672c\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actOpen_IODevice.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528QFile\u6253\u5f00\u6587\u672c\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.actOpen_TextStream.setText(QCoreApplication.translate("MainWindow", u"QTextStream\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.actOpen_TextStream.setToolTip(QCoreApplication.translate("MainWindow", u"\u7528QTextStream\u6253\u5f00\u6587\u672c\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actOpen_TextStream.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528QTextStream\u6253\u5f00\u6587\u672c\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actQuit.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#endif // QT_CONFIG(tooltip)
        self.actSave_IODevice.setText(QCoreApplication.translate("MainWindow", u"QFile\u53e6\u5b58", None))
#if QT_CONFIG(tooltip)
        self.actSave_IODevice.setToolTip(QCoreApplication.translate("MainWindow", u"\u7528QFile\u76f4\u63a5\u53e6\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actSave_IODevice.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528QFile\u76f4\u63a5\u53e6\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.actSave_TextStream.setText(QCoreApplication.translate("MainWindow", u"QTextStream\u53e6\u5b58", None))
#if QT_CONFIG(tooltip)
        self.actSave_TextStream.setToolTip(QCoreApplication.translate("MainWindow", u"\u7528QTextStream\u53e6\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actSave_TextStream.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528QTextStream\u53e6\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.actSave_TextSafe.setText(QCoreApplication.translate("MainWindow", u"QSaveFile\u53e6\u5b58", None))
#if QT_CONFIG(tooltip)
        self.actSave_TextSafe.setToolTip(QCoreApplication.translate("MainWindow", u"\u7528QSaveFile\u53e6\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actSave_TextSafe.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528QSaveFile\u53e6\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"QFile\u76f4\u63a5\u64cd\u4f5c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"QTextStream\u64cd\u4f5c", None))
    # retranslateUi

