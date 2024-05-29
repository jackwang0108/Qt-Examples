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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 604)
        self.actFileNew = QAction(MainWindow)
        self.actFileNew.setObjectName(u"actFileNew")
        icon = QIcon()
        icon.addFile(u":/icons/images/100.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFileNew.setIcon(icon)
        self.actFileNew.setMenuRole(QAction.NoRole)
        self.actFileOpen = QAction(MainWindow)
        self.actFileOpen.setObjectName(u"actFileOpen")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/001.GIF", QSize(), QIcon.Normal, QIcon.Off)
        self.actFileOpen.setIcon(icon1)
        self.actFileOpen.setMenuRole(QAction.NoRole)
        self.actFileSave = QAction(MainWindow)
        self.actFileSave.setObjectName(u"actFileSave")
        self.actFileSave.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/104.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFileSave.setIcon(icon2)
        self.actFileSave.setMenuRole(QAction.NoRole)
        self.actEditCut = QAction(MainWindow)
        self.actEditCut.setObjectName(u"actEditCut")
        self.actEditCut.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/200.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actEditCut.setIcon(icon3)
        self.actEditCut.setMenuRole(QAction.NoRole)
        self.actEditCopy = QAction(MainWindow)
        self.actEditCopy.setObjectName(u"actEditCopy")
        self.actEditCopy.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/220.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actEditCopy.setIcon(icon4)
        self.actEditCopy.setMenuRole(QAction.NoRole)
        self.actEditPaste = QAction(MainWindow)
        self.actEditPaste.setObjectName(u"actEditPaste")
        self.actEditPaste.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/204.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actEditPaste.setIcon(icon5)
        self.actEditPaste.setMenuRole(QAction.NoRole)
        self.actEditUndo = QAction(MainWindow)
        self.actEditUndo.setObjectName(u"actEditUndo")
        self.actEditUndo.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/206.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actEditUndo.setIcon(icon6)
        self.actEditUndo.setMenuRole(QAction.NoRole)
        self.actEditRedo = QAction(MainWindow)
        self.actEditRedo.setObjectName(u"actEditRedo")
        self.actEditRedo.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/208.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actEditRedo.setIcon(icon7)
        self.actEditRedo.setMenuRole(QAction.NoRole)
        self.actFontBold = QAction(MainWindow)
        self.actFontBold.setObjectName(u"actFontBold")
        self.actFontBold.setCheckable(True)
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/500.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFontBold.setIcon(icon8)
        self.actFontBold.setMenuRole(QAction.NoRole)
        self.actFontItalic = QAction(MainWindow)
        self.actFontItalic.setObjectName(u"actFontItalic")
        self.actFontItalic.setCheckable(True)
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/502.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFontItalic.setIcon(icon9)
        self.actFontItalic.setMenuRole(QAction.NoRole)
        self.actFontUnderline = QAction(MainWindow)
        self.actFontUnderline.setObjectName(u"actFontUnderline")
        self.actFontUnderline.setCheckable(True)
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/504.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFontUnderline.setIcon(icon10)
        self.actFontUnderline.setMenuRole(QAction.NoRole)
        self.actLangZh = QAction(MainWindow)
        self.actLangZh.setObjectName(u"actLangZh")
        self.actLangZh.setCheckable(True)
        self.actLangZh.setChecked(True)
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/CN.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actLangZh.setIcon(icon11)
        self.actLangZh.setMenuRole(QAction.NoRole)
        self.actLangEn = QAction(MainWindow)
        self.actLangEn.setObjectName(u"actLangEn")
        self.actLangEn.setCheckable(True)
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/timg2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actLangEn.setIcon(icon12)
        self.actLangEn.setMenuRole(QAction.NoRole)
        self.actClose = QAction(MainWindow)
        self.actClose.setObjectName(u"actClose")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/324.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actClose.setIcon(icon13)
        self.actClose.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1076, 24))
        self.menu_F = QMenu(self.menubar)
        self.menu_F.setObjectName(u"menu_F")
        self.menu_E = QMenu(self.menubar)
        self.menu_E.setObjectName(u"menu_E")
        self.menu_M = QMenu(self.menubar)
        self.menu_M.setObjectName(u"menu_M")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_M.menuAction())
        self.menu_F.addAction(self.actFileNew)
        self.menu_F.addAction(self.actFileOpen)
        self.menu_F.addAction(self.actFileSave)
        self.menu_E.addAction(self.actEditCut)
        self.menu_E.addAction(self.actEditCopy)
        self.menu_E.addAction(self.actEditPaste)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.actEditUndo)
        self.menu_E.addAction(self.actEditRedo)
        self.menu_M.addAction(self.actFontBold)
        self.menu_M.addAction(self.actFontItalic)
        self.menu_M.addAction(self.actFontUnderline)
        self.toolBar.addAction(self.actFileNew)
        self.toolBar.addAction(self.actFileOpen)
        self.toolBar.addAction(self.actFileSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actEditCut)
        self.toolBar.addAction(self.actEditCopy)
        self.toolBar.addAction(self.actEditPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actEditUndo)
        self.toolBar.addAction(self.actEditRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actFontBold)
        self.toolBar.addAction(self.actFontItalic)
        self.toolBar.addAction(self.actFontUnderline)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actLangZh)
        self.toolBar.addAction(self.actLangEn)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.actEditCut.triggered.connect(self.textEdit.cut)
        self.actEditPaste.triggered.connect(self.textEdit.paste)
        self.actEditCopy.triggered.connect(self.textEdit.copy)
        self.actEditUndo.triggered.connect(self.textEdit.undo)
        self.actEditRedo.triggered.connect(self.textEdit.redo)
        self.actClose.triggered.connect(MainWindow.close)
        self.textEdit.undoAvailable.connect(self.actEditUndo.setEnabled)
        self.textEdit.redoAvailable.connect(self.actEditRedo.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actFileNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(tooltip)
        self.actFileNew.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actFileNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actFileOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.actFileOpen.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actFileOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actFileSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.actFileSave.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actFileSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actEditCut.setText(QCoreApplication.translate("MainWindow", u"\u526a\u5207", None))
#if QT_CONFIG(tooltip)
        self.actEditCut.setToolTip(QCoreApplication.translate("MainWindow", u"\u526a\u5207\u9009\u4e2d\u6587\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actEditCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actEditCopy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.actEditCopy.setToolTip(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u9009\u4e2d\u7684\u6587\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actEditCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actEditPaste.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
#if QT_CONFIG(tooltip)
        self.actEditPaste.setToolTip(QCoreApplication.translate("MainWindow", u"\u9ecf\u8d34\u526a\u5207\u677f\u4e2d\u7684\u6587\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actEditPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actEditUndo.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500", None))
#if QT_CONFIG(tooltip)
        self.actEditUndo.setToolTip(QCoreApplication.translate("MainWindow", u"\u64a4\u9500\u4e0a\u6b21\u7f16\u8f91", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actEditUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actEditRedo.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u505a", None))
#if QT_CONFIG(tooltip)
        self.actEditRedo.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u505a\u4e0a\u6b21\u7f16\u8f91", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actEditRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actFontBold.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u7c97", None))
#if QT_CONFIG(tooltip)
        self.actFontBold.setToolTip(QCoreApplication.translate("MainWindow", u"\u52a0\u7c97\u9009\u4e2d\u6587\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actFontBold.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actFontItalic.setText(QCoreApplication.translate("MainWindow", u"\u659c\u4f53", None))
#if QT_CONFIG(tooltip)
        self.actFontItalic.setToolTip(QCoreApplication.translate("MainWindow", u"\u659c\u4f53\u9009\u4e2d\u6587\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actFontItalic.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actFontUnderline.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5212\u7ebf", None))
#if QT_CONFIG(tooltip)
        self.actFontUnderline.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e3a\u9009\u4e2d\u6587\u672c\u6dfb\u52a0\u4e0b\u5212\u7ebf", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actFontUnderline.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actLangZh.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587", None))
#if QT_CONFIG(tooltip)
        self.actLangZh.setToolTip(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u8bed\u8a00\u4e3a\u4e2d\u6587", None))
#endif // QT_CONFIG(tooltip)
        self.actLangEn.setText(QCoreApplication.translate("MainWindow", u"English", None))
#if QT_CONFIG(tooltip)
        self.actLangEn.setToolTip(QCoreApplication.translate("MainWindow", u"Change language to English", None))
#endif // QT_CONFIG(tooltip)
        self.actClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.actClose.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u7f16\u8f91\u5668", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#ifndef MAINWINDOW_H</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#define MAINWINDOW_H</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#include &lt;QMenuBar&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#include &lt;QMainWindow&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QT_BEGIN_NAMESPACE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">namespace Ui</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    class MainWindow;</p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QT_END_NAMESPACE</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">class MainWindow : public QMainWindow</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Q_OBJECT</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin"
                        "-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">public:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    MainWindow(QWidget *parent = nullptr);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    ~MainWindow();</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">private:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ui::MainWindow *ui;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">};</p>\n"
"<p"
                        " style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#endif // MAINWINDOW_H</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menu_F.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.menu_E.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91(&E)", None))
        self.menu_M.setTitle(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f(&M)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

