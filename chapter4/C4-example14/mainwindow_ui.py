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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QSplitter, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnSetHHeader = QPushButton(self.groupBox)
        self.btnSetHHeader.setObjectName(u"btnSetHHeader")

        self.gridLayout.addWidget(self.btnSetHHeader, 0, 0, 1, 2)

        self.btnSetColumns = QPushButton(self.groupBox)
        self.btnSetColumns.setObjectName(u"btnSetColumns")

        self.gridLayout.addWidget(self.btnSetColumns, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(10)

        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)

        self.btnTableInit = QPushButton(self.groupBox)
        self.btnTableInit.setObjectName(u"btnTableInit")

        self.gridLayout.addWidget(self.btnTableInit, 2, 0, 1, 2)

        self.btnTableInsert = QPushButton(self.groupBox)
        self.btnTableInsert.setObjectName(u"btnTableInsert")

        self.gridLayout.addWidget(self.btnTableInsert, 3, 0, 1, 1)

        self.btnTableAppend = QPushButton(self.groupBox)
        self.btnTableAppend.setObjectName(u"btnTableAppend")

        self.gridLayout.addWidget(self.btnTableAppend, 3, 1, 1, 1)

        self.btnTableDelete = QPushButton(self.groupBox)
        self.btnTableDelete.setObjectName(u"btnTableDelete")

        self.gridLayout.addWidget(self.btnTableDelete, 4, 0, 1, 2)

        self.btnAutoHeight = QPushButton(self.groupBox)
        self.btnAutoHeight.setObjectName(u"btnAutoHeight")

        self.gridLayout.addWidget(self.btnAutoHeight, 5, 0, 1, 1)

        self.btnAutoWidth = QPushButton(self.groupBox)
        self.btnAutoWidth.setObjectName(u"btnAutoWidth")

        self.gridLayout.addWidget(self.btnAutoWidth, 5, 1, 1, 1)

        self.btnReadtoEdit = QPushButton(self.groupBox)
        self.btnReadtoEdit.setObjectName(u"btnReadtoEdit")

        self.gridLayout.addWidget(self.btnReadtoEdit, 6, 0, 1, 2)

        self.chkTableEditable = QCheckBox(self.groupBox)
        self.chkTableEditable.setObjectName(u"chkTableEditable")
        self.chkTableEditable.setChecked(True)

        self.gridLayout.addWidget(self.chkTableEditable, 7, 0, 1, 1)

        self.chkColorRow = QCheckBox(self.groupBox)
        self.chkColorRow.setObjectName(u"chkColorRow")
        self.chkColorRow.setChecked(True)

        self.gridLayout.addWidget(self.chkColorRow, 7, 1, 1, 1)

        self.btnShowHHeader = QCheckBox(self.groupBox)
        self.btnShowHHeader.setObjectName(u"btnShowHHeader")
        self.btnShowHHeader.setChecked(True)

        self.gridLayout.addWidget(self.btnShowHHeader, 8, 0, 1, 1)

        self.btnShowVHeader = QCheckBox(self.groupBox)
        self.btnShowVHeader.setObjectName(u"btnShowVHeader")
        self.btnShowVHeader.setChecked(True)

        self.gridLayout.addWidget(self.btnShowVHeader, 8, 1, 1, 1)

        self.radioRowSelect = QRadioButton(self.groupBox)
        self.radioRowSelect.setObjectName(u"radioRowSelect")
        self.radioRowSelect.setChecked(True)

        self.gridLayout.addWidget(self.radioRowSelect, 9, 0, 1, 1)

        self.radioCellSelect = QRadioButton(self.groupBox)
        self.radioCellSelect.setObjectName(u"radioCellSelect")

        self.gridLayout.addWidget(self.radioCellSelect, 9, 1, 1, 1)

        self.splitter_2.addWidget(self.groupBox)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.tableWidget = QTableWidget(self.splitter)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.splitter.addWidget(self.tableWidget)
        self.plainTextEdit = QPlainTextEdit(self.splitter)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.splitter.addWidget(self.plainTextEdit)
        self.splitter_2.addWidget(self.splitter)

        self.horizontalLayout.addWidget(self.splitter_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.btnSetHHeader.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6c34\u5e73\u8868\u5934", None))
        self.btnSetColumns.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u884c\u6570", None))
        self.spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" \u884c", None))
        self.btnTableInit.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316\u8868\u683c\u6570\u636e", None))
        self.btnTableInsert.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u5165\u884c", None))
        self.btnTableAppend.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u884c", None))
        self.btnTableDelete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5f53\u524d\u884c", None))
        self.btnAutoHeight.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8c03\u8282\u884c\u9ad8", None))
        self.btnAutoWidth.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8c03\u8282\u5217\u5bbd", None))
        self.btnReadtoEdit.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u8868\u683c\u5185\u5bb9\u5230\u6587\u672c", None))
        self.chkTableEditable.setText(QCoreApplication.translate("MainWindow", u"\u8868\u683c\u53ef\u7f16\u8f91", None))
        self.chkColorRow.setText(QCoreApplication.translate("MainWindow", u"\u95f4\u9694\u884c\u5e95\u8272", None))
        self.btnShowHHeader.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6c34\u5e73\u8868\u5934", None))
        self.btnShowVHeader.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5782\u76f4\u8868\u5934", None))
        self.radioRowSelect.setText(QCoreApplication.translate("MainWindow", u"\u884c\u9009\u62e9", None))
        self.radioCellSelect.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5143\u683c\u9009\u62e9", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"00", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"11", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

