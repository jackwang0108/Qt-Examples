# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(693, 444)
        self.verticalLayout_11 = QVBoxLayout(Widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_top = QHBoxLayout()
        self.horizontalLayout_top.setObjectName(u"horizontalLayout_top")
        self.groupBox_setObj = QGroupBox(Widget)
        self.groupBox_setObj.setObjectName(u"groupBox_setObj")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_setObj)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioListSource = QRadioButton(self.groupBox_setObj)
        self.radioListSource.setObjectName(u"radioListSource")
        self.radioListSource.setChecked(True)

        self.verticalLayout_6.addWidget(self.radioListSource)

        self.radioListWidget = QRadioButton(self.groupBox_setObj)
        self.radioListWidget.setObjectName(u"radioListWidget")

        self.verticalLayout_6.addWidget(self.radioListWidget)

        self.radioTreeWidget = QRadioButton(self.groupBox_setObj)
        self.radioTreeWidget.setObjectName(u"radioTreeWidget")

        self.verticalLayout_6.addWidget(self.radioTreeWidget)

        self.radioTableWidget = QRadioButton(self.groupBox_setObj)
        self.radioTableWidget.setObjectName(u"radioTableWidget")

        self.verticalLayout_6.addWidget(self.radioTableWidget)


        self.horizontalLayout_top.addWidget(self.groupBox_setObj)

        self.groupBox_params = QGroupBox(Widget)
        self.groupBox_params.setObjectName(u"groupBox_params")
        self.gridLayout_2 = QGridLayout(self.groupBox_params)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(9)
        self.label_dragDropMode = QLabel(self.groupBox_params)
        self.label_dragDropMode.setObjectName(u"label_dragDropMode")

        self.gridLayout_2.addWidget(self.label_dragDropMode, 1, 0, 1, 1)

        self.chkBoxAcceptDrops = QCheckBox(self.groupBox_params)
        self.chkBoxAcceptDrops.setObjectName(u"chkBoxAcceptDrops")
        self.chkBoxAcceptDrops.setChecked(True)

        self.gridLayout_2.addWidget(self.chkBoxAcceptDrops, 0, 0, 1, 1)

        self.chkBoxDragEnabled = QCheckBox(self.groupBox_params)
        self.chkBoxDragEnabled.setObjectName(u"chkBoxDragEnabled")
        self.chkBoxDragEnabled.setChecked(True)

        self.gridLayout_2.addWidget(self.chkBoxDragEnabled, 0, 1, 1, 1)

        self.comboDefaultAction = QComboBox(self.groupBox_params)
        self.comboDefaultAction.addItem("")
        self.comboDefaultAction.addItem("")
        self.comboDefaultAction.addItem("")
        self.comboDefaultAction.addItem("")
        self.comboDefaultAction.setObjectName(u"comboDefaultAction")

        self.gridLayout_2.addWidget(self.comboDefaultAction, 2, 1, 1, 1)

        self.label_defaultDropAction = QLabel(self.groupBox_params)
        self.label_defaultDropAction.setObjectName(u"label_defaultDropAction")

        self.gridLayout_2.addWidget(self.label_defaultDropAction, 2, 0, 1, 1)

        self.comboMode = QComboBox(self.groupBox_params)
        self.comboMode.addItem("")
        self.comboMode.addItem("")
        self.comboMode.addItem("")
        self.comboMode.addItem("")
        self.comboMode.addItem("")
        self.comboMode.setObjectName(u"comboMode")
        self.comboMode.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.comboMode, 1, 1, 1, 1)


        self.horizontalLayout_top.addWidget(self.groupBox_params)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_top.addItem(self.horizontalSpacer)


        self.verticalLayout_11.addLayout(self.horizontalLayout_top)

        self.horizontalLayout_bottom = QHBoxLayout()
        self.horizontalLayout_bottom.setObjectName(u"horizontalLayout_bottom")
        self.groupBox_listSource = QGroupBox(Widget)
        self.groupBox_listSource.setObjectName(u"groupBox_listSource")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox_listSource.setFont(font)
        self.groupBox_listSource.setFlat(False)
        self.groupBox_listSource.setCheckable(False)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_listSource)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.listSource = QListWidget(self.groupBox_listSource)
        icon = QIcon()
        icon.addFile(u":/icons/images/200.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listSource)
        __qlistwidgetitem.setIcon(icon);
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/202.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listSource)
        __qlistwidgetitem1.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/204.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listSource)
        __qlistwidgetitem2.setIcon(icon2);
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/500.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listSource)
        __qlistwidgetitem3.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/502.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.listSource)
        __qlistwidgetitem4.setIcon(icon4);
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/504.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem5 = QListWidgetItem(self.listSource)
        __qlistwidgetitem5.setIcon(icon5);
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/508.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem6 = QListWidgetItem(self.listSource)
        __qlistwidgetitem6.setIcon(icon6);
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/510.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem7 = QListWidgetItem(self.listSource)
        __qlistwidgetitem7.setIcon(icon7);
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/512.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem8 = QListWidgetItem(self.listSource)
        __qlistwidgetitem8.setIcon(icon8);
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/718.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem9 = QListWidgetItem(self.listSource)
        __qlistwidgetitem9.setIcon(icon9);
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/724.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem10 = QListWidgetItem(self.listSource)
        __qlistwidgetitem10.setIcon(icon10);
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/728.bmp", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem11 = QListWidgetItem(self.listSource)
        __qlistwidgetitem11.setIcon(icon11);
        self.listSource.setObjectName(u"listSource")
        self.listSource.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listSource.setDragDropMode(QAbstractItemView.DragOnly)
        self.listSource.setAlternatingRowColors(True)
        self.listSource.setUniformItemSizes(False)
        self.listSource.setSelectionRectVisible(True)

        self.verticalLayout_8.addWidget(self.listSource)


        self.horizontalLayout_bottom.addWidget(self.groupBox_listSource)

        self.groupBox_listWidget = QGroupBox(Widget)
        self.groupBox_listWidget.setObjectName(u"groupBox_listWidget")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_listWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.listWidget = QListWidget(self.groupBox_listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget.setDefaultDropAction(Qt.CopyAction)
        self.listWidget.setViewMode(QListView.ListMode)

        self.verticalLayout_10.addWidget(self.listWidget)


        self.horizontalLayout_bottom.addWidget(self.groupBox_listWidget)

        self.groupBox_treeWidget = QGroupBox(Widget)
        self.groupBox_treeWidget.setObjectName(u"groupBox_treeWidget")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_treeWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.treeWidget = QTreeWidget(self.groupBox_treeWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setAcceptDrops(True)
        self.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeWidget.setDragDropOverwriteMode(True)
        self.treeWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeWidget.setDefaultDropAction(Qt.MoveAction)
        self.treeWidget.header().setVisible(False)

        self.verticalLayout_9.addWidget(self.treeWidget)


        self.horizontalLayout_bottom.addWidget(self.groupBox_treeWidget)

        self.groupBox_tableWidget = QGroupBox(Widget)
        self.groupBox_tableWidget.setObjectName(u"groupBox_tableWidget")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_tableWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.tableWidget = QTableWidget(self.groupBox_tableWidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(180, 0))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropMode(QAbstractItemView.DropOnly)
        self.tableWidget.setDefaultDropAction(Qt.CopyAction)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.verticalHeader().setDefaultSectionSize(29)

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.horizontalLayout_bottom.addWidget(self.groupBox_tableWidget)


        self.verticalLayout_11.addLayout(self.horizontalLayout_bottom)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u5177\u6709DragDrop\u529f\u80fd\u7684\u7ec4\u4ef6", None))
        self.groupBox_setObj.setTitle(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e\u5bf9\u8c61", None))
        self.radioListSource.setText(QCoreApplication.translate("Widget", u"listSource", None))
        self.radioListWidget.setText(QCoreApplication.translate("Widget", u"listWidget", None))
        self.radioTreeWidget.setText(QCoreApplication.translate("Widget", u"treeWidget", None))
        self.radioTableWidget.setText(QCoreApplication.translate("Widget", u"tableWidget", None))
        self.groupBox_params.setTitle(QCoreApplication.translate("Widget", u"\u62d6\u653e\u53c2\u6570", None))
        self.label_dragDropMode.setText(QCoreApplication.translate("Widget", u"dragDropMode", None))
        self.chkBoxAcceptDrops.setText(QCoreApplication.translate("Widget", u"acceptDrops", None))
        self.chkBoxDragEnabled.setText(QCoreApplication.translate("Widget", u"dragEnabled", None))
        self.comboDefaultAction.setItemText(0, QCoreApplication.translate("Widget", u"CopyAction", None))
        self.comboDefaultAction.setItemText(1, QCoreApplication.translate("Widget", u"MoveAction", None))
        self.comboDefaultAction.setItemText(2, QCoreApplication.translate("Widget", u"LinkAction", None))
        self.comboDefaultAction.setItemText(3, QCoreApplication.translate("Widget", u"IgnoreAction", None))

        self.label_defaultDropAction.setText(QCoreApplication.translate("Widget", u"defaultDropAction", None))
        self.comboMode.setItemText(0, QCoreApplication.translate("Widget", u"NoDragDrop", None))
        self.comboMode.setItemText(1, QCoreApplication.translate("Widget", u"DragOnly", None))
        self.comboMode.setItemText(2, QCoreApplication.translate("Widget", u"DropOnly", None))
        self.comboMode.setItemText(3, QCoreApplication.translate("Widget", u"DragDrop", None))
        self.comboMode.setItemText(4, QCoreApplication.translate("Widget", u"InternalMove", None))

        self.groupBox_listSource.setTitle(QCoreApplication.translate("Widget", u"listSource", None))

        __sortingEnabled = self.listSource.isSortingEnabled()
        self.listSource.setSortingEnabled(False)
        ___qlistwidgetitem = self.listSource.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Widget", u"\u526a\u5207", None));
        ___qlistwidgetitem1 = self.listSource.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Widget", u"\u590d\u5236", None));
        ___qlistwidgetitem2 = self.listSource.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Widget", u"\u7c98\u8d34", None));
        ___qlistwidgetitem3 = self.listSource.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Widget", u"\u7c97\u4f53", None));
        ___qlistwidgetitem4 = self.listSource.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Widget", u"\u659c\u4f53", None));
        ___qlistwidgetitem5 = self.listSource.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Widget", u"\u4e0b\u5212\u7ebf", None));
        ___qlistwidgetitem6 = self.listSource.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Widget", u"\u5de6\u5bf9\u9f50", None));
        ___qlistwidgetitem7 = self.listSource.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Widget", u"\u4e2d\u95f4\u5bf9\u9f50", None));
        ___qlistwidgetitem8 = self.listSource.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Widget", u"\u53f3\u5bf9\u9f50", None));
        ___qlistwidgetitem9 = self.listSource.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Widget", u"\u7ea2\u8272", None));
        ___qlistwidgetitem10 = self.listSource.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Widget", u"\u7eff\u8272", None));
        ___qlistwidgetitem11 = self.listSource.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Widget", u"\u84dd\u8272", None));
        self.listSource.setSortingEnabled(__sortingEnabled)

        self.groupBox_listWidget.setTitle(QCoreApplication.translate("Widget", u"listWidget", None))
        self.groupBox_treeWidget.setTitle(QCoreApplication.translate("Widget", u"treeWidget", None))
        self.groupBox_tableWidget.setTitle(QCoreApplication.translate("Widget", u"tableWidget", None))
    # retranslateUi

