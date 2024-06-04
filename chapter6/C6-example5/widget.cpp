#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    itemView = ui->listSource;
    refreshUI(ui->groupBox_listSource);

    ui->listSource->setAcceptDrops(true);
    ui->listSource->setDragEnabled(true);
    ui->listSource->setDefaultDropAction(Qt::CopyAction);
    ui->listSource->setDragDropMode(QAbstractItemView::DragDrop);

    ui->listWidget->setAcceptDrops(true);
    ui->listWidget->setDragEnabled(true);
    ui->listWidget->setDefaultDropAction(Qt::CopyAction);
    ui->listWidget->setDragDropMode(QAbstractItemView::DragDrop);

    ui->treeWidget->setAcceptDrops(true);
    ui->treeWidget->setDragEnabled(true);
    ui->treeWidget->setDefaultDropAction(Qt::CopyAction);
    ui->treeWidget->setDragDropMode(QAbstractItemView::DragDrop);

    ui->tableWidget->setAcceptDrops(true);
    ui->tableWidget->setDragEnabled(true);
    ui->tableWidget->setDefaultDropAction(Qt::CopyAction);
    ui->tableWidget->setDragDropMode(QAbstractItemView::DragDrop);

    ui->listSource->installEventFilter(this);
    ui->listWidget->installEventFilter(this);
    ui->treeWidget->installEventFilter(this);
    ui->tableWidget->installEventFilter(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::refreshUI(QGroupBox *box)
{
    ui->chkBoxAcceptDrops->setChecked(itemView->acceptDrops());
    ui->chkBoxDragEnabled->setChecked(itemView->dragEnabled());

    ui->comboMode->setCurrentIndex((int)itemView->dragDropMode());
    int index = getDropActionIndex(itemView->defaultDropAction());
    ui->comboDefaultAction->setCurrentIndex(index);

    QFont font = ui->groupBox_listSource->font();

    font.setBold(false);
    ui->groupBox_listSource->setFont(font);
    ui->groupBox_listWidget->setFont(font);
    ui->groupBox_tableWidget->setFont(font);
    ui->groupBox_treeWidget->setFont(font);

    font.setBold(true);
    box->setFont(font);
}

// comboBox的索引转换为DropAction类型
Qt::DropAction Widget::getDropActionType(int index)
{
    // CopyAction = 0x1
    // MoveAction = 0x2
    // LinkAction = 0x4
    // IgnoreAction = 0x0
    switch (index)
    {
    case 0:
        return Qt::CopyAction;
    case 1:
        return Qt::MoveAction;
    case 2:
        return Qt::LinkAction;
    case 3:
        return Qt::IgnoreAction;
    default:
        return Qt::CopyAction;
    }
}

// DropAction类型转换为comboBox的索引
int Widget::getDropActionIndex(Qt::DropAction actionType)
{
    switch (actionType)
    {
    case Qt::CopyAction:
        return 0;
    case Qt::MoveAction:
        return 1;
    case Qt::LinkAction:
        return 2;
    case Qt::IgnoreAction:
        return 3;
    default:
        return 0;
    }
}

void Widget::on_radioListSource_clicked()
{
    itemView = ui->listSource;
    refreshUI(ui->groupBox_listSource);
}

void Widget::on_radioListWidget_clicked()
{
    itemView = ui->listWidget;
    refreshUI(ui->groupBox_listWidget);
}

void Widget::on_radioTreeWidget_clicked()
{
    itemView = ui->treeWidget;
    refreshUI(ui->groupBox_treeWidget);
}

void Widget::on_radioTableWidget_clicked()
{
    itemView = ui->tableWidget;
    refreshUI(ui->groupBox_tableWidget);
}

void Widget::on_chkBoxAcceptDrops_clicked(bool checked)
{
    itemView->setAcceptDrops(checked);
}

void Widget::on_chkBoxDragEnabled_clicked(bool checked)
{
    itemView->setDragEnabled(checked);
}

void Widget::on_comboMode_currentIndexChanged(int index)
{
    itemView->setDragDropMode((QAbstractItemView::DragDropMode)index);
}

void Widget::on_comboDefaultAction_currentIndexChanged(int index)
{
    Qt::DropAction action = getDropActionType(index);

    itemView->setDefaultDropAction(action);
}

bool Widget::eventFilter(QObject *watched, QEvent *event)
{
    if (event->type() != QEvent::KeyPress)
        return QWidget::eventFilter(watched, event);

    qDebug() << "KeyPressed";

    QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
    if (keyEvent->key() != Qt::Key_Backspace)
        return QWidget::eventFilter(watched, event);

    qDebug() << "KeyDelete";

    if (watched == ui->listSource)
        delete ui->listSource->takeItem(ui->listSource->currentRow());
    else if (watched == ui->listWidget)
        delete ui->listWidget->takeItem(ui->listWidget->currentRow());
    else if (watched == ui->treeWidget)
    {
        QTreeWidgetItem *currItem = ui->treeWidget->currentItem();
        if (currItem != nullptr)
        {
            QTreeWidgetItem *parentItem = currItem->parent();
            if (parentItem)
                parentItem->removeChild(currItem);
            else
            {
                int index = ui->treeWidget->indexOfTopLevelItem(currItem);
                if (index != -1)
                {
                    delete ui->treeWidget->takeTopLevelItem(index);
                }
            }
        }
    }
    else if (watched == ui->tableWidget)
        delete ui->tableWidget->item(ui->tableWidget->currentRow(), ui->tableWidget->currentColumn());

    return QWidget::eventFilter(watched, event);
}
