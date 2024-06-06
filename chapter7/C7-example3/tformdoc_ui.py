# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tformdoc.ui'
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
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QSizePolicy, QWidget)
import res_rc

class Ui_TFormDoc(object):
    def setupUi(self, TFormDoc):
        if not TFormDoc.objectName():
            TFormDoc.setObjectName(u"TFormDoc")
        TFormDoc.resize(400, 300)
        self.actPaste = QAction(TFormDoc)
        self.actPaste.setObjectName(u"actPaste")
        icon = QIcon()
        icon.addFile(u":/images/images/204.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actPaste.setIcon(icon)
        self.actPaste.setMenuRole(QAction.NoRole)
        self.actFont = QAction(TFormDoc)
        self.actFont.setObjectName(u"actFont")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/506.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actFont.setIcon(icon1)
        self.actFont.setMenuRole(QAction.NoRole)
        self.actClose = QAction(TFormDoc)
        self.actClose.setObjectName(u"actClose")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/132.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actClose.setIcon(icon2)
        self.actClose.setMenuRole(QAction.NoRole)
        self.actUndo = QAction(TFormDoc)
        self.actUndo.setObjectName(u"actUndo")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/206.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actUndo.setIcon(icon3)
        self.actUndo.setMenuRole(QAction.NoRole)
        self.actRedo = QAction(TFormDoc)
        self.actRedo.setObjectName(u"actRedo")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/208.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actRedo.setIcon(icon4)
        self.actRedo.setMenuRole(QAction.NoRole)
        self.actSave = QAction(TFormDoc)
        self.actSave.setObjectName(u"actSave")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/104.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actSave.setIcon(icon5)
        self.actSave.setMenuRole(QAction.NoRole)
        self.actCut = QAction(TFormDoc)
        self.actCut.setObjectName(u"actCut")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/200.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actCut.setIcon(icon6)
        self.actCut.setMenuRole(QAction.NoRole)
        self.actCopy = QAction(TFormDoc)
        self.actCopy.setObjectName(u"actCopy")
        icon7 = QIcon()
        icon7.addFile(u":/images/images/202.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actCopy.setIcon(icon7)
        self.actCopy.setMenuRole(QAction.NoRole)
        self.actOpen = QAction(TFormDoc)
        self.actOpen.setObjectName(u"actOpen")
        icon8 = QIcon()
        icon8.addFile(u":/images/images/122.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.actOpen.setIcon(icon8)
        self.actOpen.setMenuRole(QAction.NoRole)
        self.plainTextEdit = QPlainTextEdit(TFormDoc)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(50, 90, 311, 171))

        self.retranslateUi(TFormDoc)
        self.actCopy.triggered.connect(self.plainTextEdit.copy)
        self.actRedo.triggered.connect(self.plainTextEdit.redo)
        self.actUndo.triggered.connect(self.plainTextEdit.undo)
        self.actCut.triggered.connect(self.plainTextEdit.cut)
        self.actPaste.triggered.connect(self.plainTextEdit.paste)
        self.actClose.triggered.connect(self.plainTextEdit.close)

        QMetaObject.connectSlotsByName(TFormDoc)
    # setupUi

    def retranslateUi(self, TFormDoc):
        TFormDoc.setWindowTitle(QCoreApplication.translate("TFormDoc", u"Form", None))
        self.actPaste.setText(QCoreApplication.translate("TFormDoc", u"\u7c98\u8d34", None))
#if QT_CONFIG(shortcut)
        self.actPaste.setShortcut(QCoreApplication.translate("TFormDoc", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actFont.setText(QCoreApplication.translate("TFormDoc", u"\u5b57\u4f53", None))
#if QT_CONFIG(tooltip)
        self.actFont.setToolTip(QCoreApplication.translate("TFormDoc", u"\u5b57\u4f53", None))
#endif // QT_CONFIG(tooltip)
        self.actClose.setText(QCoreApplication.translate("TFormDoc", u"\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.actClose.setToolTip(QCoreApplication.translate("TFormDoc", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.actUndo.setText(QCoreApplication.translate("TFormDoc", u"\u64a4\u9500", None))
#if QT_CONFIG(tooltip)
        self.actUndo.setToolTip(QCoreApplication.translate("TFormDoc", u"\u64a4\u9500", None))
#endif // QT_CONFIG(tooltip)
        self.actRedo.setText(QCoreApplication.translate("TFormDoc", u"\u91cd\u505a", None))
#if QT_CONFIG(tooltip)
        self.actRedo.setToolTip(QCoreApplication.translate("TFormDoc", u"\u91cd\u505a", None))
#endif // QT_CONFIG(tooltip)
        self.actSave.setText(QCoreApplication.translate("TFormDoc", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.actSave.setToolTip(QCoreApplication.translate("TFormDoc", u"\u4fdd\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.actCut.setText(QCoreApplication.translate("TFormDoc", u"\u526a\u5207", None))
#if QT_CONFIG(tooltip)
        self.actCut.setToolTip(QCoreApplication.translate("TFormDoc", u"\u526a\u5207", None))
#endif // QT_CONFIG(tooltip)
        self.actCopy.setText(QCoreApplication.translate("TFormDoc", u"\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.actCopy.setToolTip(QCoreApplication.translate("TFormDoc", u"\u590d\u5236", None))
#endif // QT_CONFIG(tooltip)
        self.actOpen.setText(QCoreApplication.translate("TFormDoc", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.actOpen.setToolTip(QCoreApplication.translate("TFormDoc", u"\u6253\u5f00", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

