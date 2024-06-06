# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TFormTable.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QSizePolicy,
    QStatusBar, QTableView, QToolBar, QWidget)
import res_rc

class Ui_TFormTable(object):
    def setupUi(self, TFormTable):
        if not TFormTable.objectName():
            TFormTable.setObjectName(u"TFormTable")
        TFormTable.resize(800, 600)
        self.actTabSetSize = QAction(TFormTable)
        self.actTabSetSize.setObjectName(u"actTabSetSize")
        icon = QIcon()
        icon.addFile(u":/images/images/230.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actTabSetSize.setIcon(icon)
        self.actTabSetSize.setMenuRole(QAction.NoRole)
        self.actTabSetHeader = QAction(TFormTable)
        self.actTabSetHeader.setObjectName(u"actTabSetHeader")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/516.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actTabSetHeader.setIcon(icon1)
        self.actTabSetHeader.setMenuRole(QAction.NoRole)
        self.actFileQuit = QAction(TFormTable)
        self.actFileQuit.setObjectName(u"actFileQuit")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/132.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFileQuit.setIcon(icon2)
        self.actFileQuit.setMenuRole(QAction.NoRole)
        self.actTabLocate = QAction(TFormTable)
        self.actTabLocate.setObjectName(u"actTabLocate")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/304.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actTabLocate.setIcon(icon3)
        self.actTabLocate.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(TFormTable)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(250, 130, 256, 192))
        TFormTable.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TFormTable)
        self.statusbar.setObjectName(u"statusbar")
        TFormTable.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(TFormTable)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        TFormTable.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actTabSetSize)
        self.toolBar.addAction(self.actTabSetHeader)
        self.toolBar.addAction(self.actTabLocate)
        self.toolBar.addAction(self.actFileQuit)

        self.retranslateUi(TFormTable)
        self.actFileQuit.triggered.connect(TFormTable.close)

        QMetaObject.connectSlotsByName(TFormTable)
    # setupUi

    def retranslateUi(self, TFormTable):
        TFormTable.setWindowTitle(QCoreApplication.translate("TFormTable", u"MainWindow", None))
        self.actTabSetSize.setText(QCoreApplication.translate("TFormTable", u"\u8bbe\u7f6e\u8868\u683c\u7684\u884c\u5217\u6570", None))
#if QT_CONFIG(tooltip)
        self.actTabSetSize.setToolTip(QCoreApplication.translate("TFormTable", u"\u8bbe\u7f6e\u8868\u683c\u7684\u884c\u5217\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.actTabSetHeader.setText(QCoreApplication.translate("TFormTable", u"\u8bbe\u7f6e\u8868\u683c\u8868\u5934", None))
#if QT_CONFIG(tooltip)
        self.actTabSetHeader.setToolTip(QCoreApplication.translate("TFormTable", u"\u8bbe\u7f6e\u8868\u683c\u8868\u5934", None))
#endif // QT_CONFIG(tooltip)
        self.actFileQuit.setText(QCoreApplication.translate("TFormTable", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actFileQuit.setToolTip(QCoreApplication.translate("TFormTable", u"\u9000\u51fa", None))
#endif // QT_CONFIG(tooltip)
        self.actTabLocate.setText(QCoreApplication.translate("TFormTable", u"\u5b9a\u4f4d\u5355\u5143\u683c", None))
#if QT_CONFIG(tooltip)
        self.actTabLocate.setToolTip(QCoreApplication.translate("TFormTable", u"\u5b9a\u4f4d\u5355\u5143\u683c", None))
#endif // QT_CONFIG(tooltip)
        self.toolBar.setWindowTitle(QCoreApplication.translate("TFormTable", u"toolBar", None))
    # retranslateUi

