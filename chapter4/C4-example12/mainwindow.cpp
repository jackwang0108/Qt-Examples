#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->tBtnListInit->setDefaultAction(ui->actListInit);
    ui->tBtnListClear->setDefaultAction(ui->actListClear);
    ui->tBtnListAppend->setDefaultAction(ui->actListAppend);
    ui->tBtnListInsert->setDefaultAction(ui->actListInsert);
    ui->tBtnListDelete->setDefaultAction(ui->actListRemove);

    ui->tBtnSelAll->setDefaultAction(ui->actSelAll);
    ui->tBtnSelInv->setDefaultAction(ui->actSelInv);
    ui->tBtnSelNone->setDefaultAction(ui->actSelNone);

    QMenu *menu = new QMenu(this);
    menu->addAction(ui->actSelAll);
    menu->addAction(ui->actSelInv);
    menu->addAction(ui->actSelNone);

    ui->tBtnSelItem->setPopupMode(QToolButton::MenuButtonPopup);
    ui->tBtnSelItem->setMenu(menu);

    QToolButton *tBtn = new QToolButton(this);
    tBtn->setPopupMode(QToolButton::InstantPopup);
    tBtn->setText("选择选项");
    tBtn->setIcon(QIcon(":/images/icons/424.bmp"));
    tBtn->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
    tBtn->setMenu(menu);
    ui->toolBar->addWidget(tBtn);

    ui->toolBar->addSeparator();
    ui->toolBar->addAction(ui->actQuit);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actListInit_triggered()
{
    ui->listWidget->clear();

    QIcon itemIcon;
    itemIcon.addFile(":/images/icons/check2.ico");

    bool itemEditable = ui->chkListEditable->isChecked();
    for (int i = 0; i < 10; i++)
    {
        QListWidgetItem *newItem = new QListWidgetItem();

        newItem->setIcon(itemIcon);
        newItem->setText(QString::number(i));
        newItem->setCheckState(Qt::Checked);

        QFlags itemFlag =
            Qt::ItemIsSelectable |
            Qt::ItemIsUserCheckable |
            Qt::ItemIsEnabled;

        if (itemEditable)
            itemFlag |= Qt::ItemIsEditable;

        newItem->setFlags(itemFlag);

        ui->listWidget->addItem(newItem);
    }
}
void MainWindow::on_actListClear_triggered()
{
    ui->listWidget->clear();
}

void MainWindow::on_actListInsert_triggered()
{
    QIcon itemIcon;
    itemIcon.addFile(":/images/icons/check2.ico");

    bool itemEditable = ui->chkListEditable->isChecked();
    QListWidgetItem *newItem = new QListWidgetItem();

    newItem->setIcon(itemIcon);
    newItem->setText("Item Inserted");
    newItem->setCheckState(Qt::Checked);

    QFlags itemFlag =
        Qt::ItemIsSelectable |
        Qt::ItemIsUserCheckable |
        Qt::ItemIsEnabled;

    if (itemEditable)
        itemFlag |= Qt::ItemIsEditable;

    newItem->setFlags(itemFlag);

    ui->listWidget->insertItem(ui->listWidget->currentRow(), newItem);
}

void MainWindow::on_actListAppend_triggered()
{
    QIcon itemIcon;
    itemIcon.addFile(":/images/icons/check2.ico");

    bool itemEditable = ui->chkListEditable->isChecked();
    QListWidgetItem *newItem = new QListWidgetItem();

    newItem->setIcon(itemIcon);
    newItem->setText("Item Inserted");
    newItem->setCheckState(Qt::Checked);

    QFlags itemFlag =
        Qt::ItemIsSelectable |
        Qt::ItemIsUserCheckable |
        Qt::ItemIsEnabled;

    if (itemEditable)
        itemFlag |= Qt::ItemIsEditable;

    newItem->setFlags(itemFlag);

    ui->listWidget->addItem(newItem);
}

void MainWindow::on_actListRemove_triggered()
{
    int row = ui->listWidget->currentRow();
    delete ui->listWidget->takeItem(row);
}

void MainWindow::on_actSelAll_triggered()
{
    int numItems = ui->listWidget->count();
    for (int i = 0; i < numItems; i++)
    {
        QListWidgetItem *item = ui->listWidget->item(i);
        item->setCheckState(Qt::Checked);
    }
}

void MainWindow::on_actSelNone_triggered()
{
    int numItems = ui->listWidget->count();
    for (int i = 0; i < numItems; i++)
    {
        QListWidgetItem *item = ui->listWidget->item(i);
        item->setCheckState(Qt::Unchecked);
    }
}

void MainWindow::on_actSelInv_triggered()
{
    int numItems = ui->listWidget->count();
    for (int i = 0; i < numItems; i++)
    {
        QListWidgetItem *item = ui->listWidget->item(i);
        item->setCheckState(item->checkState() == Qt::Checked ? Qt::Unchecked : Qt::Checked);
    }
}

void MainWindow::on_listWidget_currentItemChanged(QListWidgetItem *current, QListWidgetItem *previous)
{
    QString str;
    if (current != nullptr)
    {
        str = "当前项: " + current->text();
        if (previous != nullptr)
            str += "前一项: " + previous->text();
        ui->editCurrentItemText->setText(str);
    }

    ui->plainTextEdit->appendPlainText("currentItemChanged()信号被触发");
}

void MainWindow::on_chkSortEnable_clicked(bool checked)
{
    ui->listWidget->setSortingEnabled(checked);
}

void MainWindow::on_tBtnSortAsc_clicked()
{
    ui->listWidget->sortItems(Qt::AscendingOrder);
}

void MainWindow::on_tBtnSortDes_clicked()
{
    ui->listWidget->sortItems(Qt::DescendingOrder);
}

void MainWindow::on_tBtnTextClear_clicked()
{
    ui->plainTextEdit->clear();
}

void MainWindow::on_tBtnTextAddLine_clicked()
{
    ui->plainTextEdit->appendPlainText("");
}

void MainWindow::on_listWidget_itemDoubleClicked(QListWidgetItem *item)
{
    ui->plainTextEdit->appendPlainText(item->text() + "被双击了");
}

void MainWindow::on_listWidget_customContextMenuRequested(const QPoint &pos)
{
    Q_UNUSED(pos);

    QMenu *menu = new QMenu(this);
    menu->addAction(ui->actListInit);
    menu->addAction(ui->actListClear);
    menu->addAction(ui->actListAppend);
    menu->addAction(ui->actListRemove);
    menu->addSeparator();
    menu->addAction(ui->actSelAll);
    menu->addAction(ui->actSelNone);
    menu->addAction(ui->actSelInv);

    menu->exec(QCursor::pos());

    delete menu;
}
