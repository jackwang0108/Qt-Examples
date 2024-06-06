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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QSizePolicy,
    QStatusBar, QToolBar, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 480)
        font = QFont()
        font.setFamilies([u"Hiragino Sans GB"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actDoc_New = QAction(MainWindow)
        self.actDoc_New.setObjectName(u"actDoc_New")
        icon = QIcon()
        icon.addFile(u":/images/images/100.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actDoc_New.setIcon(icon)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/132.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actQuit.setIcon(icon1)
        self.actDoc_Open = QAction(MainWindow)
        self.actDoc_Open.setObjectName(u"actDoc_Open")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/122.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actDoc_Open.setIcon(icon2)
        self.actFont = QAction(MainWindow)
        self.actFont.setObjectName(u"actFont")
        self.actFont.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/images/images/506.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFont.setIcon(icon3)
        self.actCut = QAction(MainWindow)
        self.actCut.setObjectName(u"actCut")
        self.actCut.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/images/images/200.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actCut.setIcon(icon4)
        self.actCopy = QAction(MainWindow)
        self.actCopy.setObjectName(u"actCopy")
        self.actCopy.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/images/images/202.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actCopy.setIcon(icon5)
        self.actPaste = QAction(MainWindow)
        self.actPaste.setObjectName(u"actPaste")
        self.actPaste.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/images/images/204.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actPaste.setIcon(icon6)
        self.actViewMode = QAction(MainWindow)
        self.actViewMode.setObjectName(u"actViewMode")
        self.actViewMode.setCheckable(True)
        icon7 = QIcon()
        icon7.addFile(u":/images/images/230.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actViewMode.setIcon(icon7)
        self.actCascade = QAction(MainWindow)
        self.actCascade.setObjectName(u"actCascade")
        icon8 = QIcon()
        icon8.addFile(u":/images/images/400.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actCascade.setIcon(icon8)
        self.actTile = QAction(MainWindow)
        self.actTile.setObjectName(u"actTile")
        icon9 = QIcon()
        icon9.addFile(u":/images/images/406.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actTile.setIcon(icon9)
        self.actCloseALL = QAction(MainWindow)
        self.actCloseALL.setObjectName(u"actCloseALL")
        icon10 = QIcon()
        icon10.addFile(u":/images/images/128.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actCloseALL.setIcon(icon10)
        self.actDoc_Save = QAction(MainWindow)
        self.actDoc_Save.setObjectName(u"actDoc_Save")
        icon11 = QIcon()
        icon11.addFile(u":/images/images/104.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actDoc_Save.setIcon(icon11)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.mdiArea = QMdiArea(self.centralWidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(30, 20, 371, 186))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setAutoFillBackground(True)
        self.mainToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.mainToolBar.addAction(self.actDoc_New)
        self.mainToolBar.addAction(self.actDoc_Open)
        self.mainToolBar.addAction(self.actDoc_Save)
        self.mainToolBar.addAction(self.actCloseALL)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actCut)
        self.mainToolBar.addAction(self.actCopy)
        self.mainToolBar.addAction(self.actPaste)
        self.mainToolBar.addAction(self.actFont)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actViewMode)
        self.mainToolBar.addAction(self.actCascade)
        self.mainToolBar.addAction(self.actTile)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MDI\u5e94\u7528\u7a0b\u5e8f", None))
        self.actDoc_New.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(tooltip)
        self.actDoc_New.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u6587\u6863\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actDoc_New.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actQuit.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u672c\u7cfb\u7edf", None))
#endif // QT_CONFIG(tooltip)
        self.actDoc_Open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.actDoc_Open.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u6863", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actDoc_Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actFont.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.actFont.setToolTip(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.actCut.setText(QCoreApplication.translate("MainWindow", u"\u526a\u5207", None))
#if QT_CONFIG(tooltip)
        self.actCut.setToolTip(QCoreApplication.translate("MainWindow", u"\u526a\u5207", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actCopy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.actCopy.setToolTip(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actPaste.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
#if QT_CONFIG(tooltip)
        self.actPaste.setToolTip(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actViewMode.setText(QCoreApplication.translate("MainWindow", u"MDI\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.actViewMode.setToolTip(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u6a21\u5f0f\u6216\u9875\u9762\u6a21\u5f0f", None))
#endif // QT_CONFIG(tooltip)
        self.actCascade.setText(QCoreApplication.translate("MainWindow", u"\u7ea7\u8054\u5c55\u5f00", None))
#if QT_CONFIG(tooltip)
        self.actCascade.setToolTip(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u7ea7\u8054\u5c55\u5f00", None))
#endif // QT_CONFIG(tooltip)
        self.actTile.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u94fa\u5c55\u5f00", None))
#if QT_CONFIG(tooltip)
        self.actTile.setToolTip(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u5e73\u94fa\u5c55\u5f00", None))
#endif // QT_CONFIG(tooltip)
        self.actCloseALL.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u5168\u90e8", None))
#if QT_CONFIG(tooltip)
        self.actCloseALL.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6240\u6709\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.actDoc_Save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.actDoc_Save.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fee\u6539", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actDoc_Save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

