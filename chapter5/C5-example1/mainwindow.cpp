#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    strList << "北京"
            << "上海"
            << "南昌"
            << "南京"
            << "成都";

    strListModel = new QStringListModel(this);
    strListModel->setStringList(strList);
    ui->listView->setModel(strListModel);
    ui->listView->setEditTriggers(
        QAbstractItemView::DoubleClicked | QAbstractItemView::SelectedClicked);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnIniList_clicked()
{
    strListModel->setStringList(strList);
}

void MainWindow::on_btnListClear_clicked()
{
    strListModel->removeRows(0, strListModel->rowCount());
}

void MainWindow::on_btnListAppend_clicked()
{
    strListModel->insertRow(strListModel->rowCount());
    QModelIndex index = strListModel->index(strListModel->rowCount() - 1);

    strListModel->setData(index, "New Row", Qt::DisplayRole);
    ui->listView->setCurrentIndex(index);
}

void MainWindow::on_btnListInsert_clicked()
{
    QModelIndex currIndex = ui->listView->currentIndex();
    strListModel->insertRow(currIndex.row());

    strListModel->setData(currIndex, "New Row", Qt::DisplayRole);
    ui->listView->setCurrentIndex(currIndex);
}

void MainWindow::on_btnListDelete_clicked()
{
}

void MainWindow::on_btnListMoveUp_clicked()
{
    QModelIndex index;
    int currRow = ui->listView->currentIndex().row();
    strListModel->moveRow(index, currRow, index, currRow - 1);
}

void MainWindow::on_btnListMoveDown_clicked()
{
    QModelIndex index;
    int currRow = ui->listView->currentIndex().row();
    strListModel->moveRow(index, currRow, index, currRow + 2);
}

void MainWindow::on_btnListSort_clicked(bool checked)
{
    if (checked)
        strListModel->sort(0, Qt::AscendingOrder);
    else
        strListModel->sort(0, Qt::DescendingOrder);
}

void MainWindow::on_chkEditable_clicked(bool checked)
{

    QFlags<QAbstractItemView::EditTrigger> editable;

    if (checked)
        editable = QAbstractItemView::DoubleClicked | QAbstractItemView::SelectedClicked;
    else
        editable = QAbstractItemView::NoEditTriggers;

    ui->listView->setEditTriggers(editable);
}

void MainWindow::on_btnTextClear_clicked()
{
    ui->plainTextEdit->clear();
}

void MainWindow::on_btnTextImport_clicked()
{
    on_btnTextClear_clicked();

    QStringList temp = strListModel->stringList();
    for (int i = 0; i < temp.size(); i++)
        ui->plainTextEdit->appendPlainText(temp[i]);
}

void MainWindow::on_listView_clicked(const QModelIndex &index)
{
    QString str = QString::asprintf("模型索引: row=%d, col=%d, 内容: ", index.row(), index.column());
    str += strListModel->data(index, Qt::DisplayRole).toString();
    ui->statusbar->showMessage(str);
}
