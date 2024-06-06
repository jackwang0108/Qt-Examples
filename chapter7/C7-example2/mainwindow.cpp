#include "mainwindow.h"
#include "tdialogsize.h"
#include "tdialoglocate.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setCentralWidget(ui->tableView);

    model = new QStandardItemModel(4, 4, this);
    select = new QItemSelectionModel(model);

    QStringList header{"姓名", "性别", "学位", "部分"};
    model->setHorizontalHeaderLabels(header);

    ui->tableView->setModel(model);
    ui->tableView->setSelectionModel(select);

    dlgHeader = new TDialogHeaders(this);

    labelCellPos = new QLabel("当前单元格: ", this);
    labelCellPos->setMinimumWidth(200);
    labelCellText = new QLabel("单元格内容: ", this);
    labelCellText->setMinimumWidth(200);

    ui->statusbar->addWidget(labelCellPos);
    ui->statusbar->addWidget(labelCellText);

    connect(select, &QItemSelectionModel::currentChanged, this, &MainWindow::on_model_currentChanged);
}

MainWindow::~MainWindow()
{
    delete ui;

    delete dlgHeader;
}

void MainWindow::on_actTabSetSize_triggered()
{
    TDialogSize *dlgTableSize = new TDialogSize();

    dlgTableSize->setRowCol(model->rowCount(), model->columnCount());
    dlgTableSize->setWindowFlag(Qt::MSWindowsFixedSizeDialogHint);

    int ret = dlgTableSize->exec();
    if (ret == QDialog::Accepted)
    {
        model->setColumnCount(dlgTableSize->colCount());
        model->setRowCount(dlgTableSize->rowCount());
    }
    delete dlgTableSize;
}

void MainWindow::on_actTabSetHeader_triggered()
{
    QStringList headers;

    for (int i = 0; i < model->columnCount(); i++)
        headers.append(model->headerData(i, Qt::Horizontal, Qt::DisplayRole).toString());

    dlgHeader->setHeaderList(headers);

    int ret = dlgHeader->exec();
    if (ret == QDialog::Accepted)
        model->setHorizontalHeaderLabels(dlgHeader->headerList());
}

void MainWindow::on_actTabLocate_triggered()
{
    TDialogLocate *dlgLocate = new TDialogLocate(this);
    dlgLocate->setAttribute(Qt::WA_DeleteOnClose);
    dlgLocate->setWindowFlag(Qt::WindowStaysOnTopHint);

    // 初始化对话框
    dlgLocate->setSpinRange(model->rowCount(), model->columnCount());

    QModelIndex currIndex = select->currentIndex();
    if (currIndex.isValid())
        dlgLocate->setSpinValue(currIndex.row(), currIndex.column());

    connect(dlgLocate, &TDialogLocate::cellTextChanged, this, &MainWindow::do_setCellText);
    connect(dlgLocate, &TDialogLocate::changeActionEnabled, ui->actTabLocate, &QAction::setEnabled);
    connect(this, &MainWindow::cellIndexChanged, dlgLocate, &TDialogLocate::setSpinValue);

    dlgLocate->show();
    dlgLocate->setModal(false);
}

void MainWindow::do_setCellText(int row, int col, QString &text)
{
    QModelIndex index = model->index(row, col);
    select->clearSelection();
    select->setCurrentIndex(index, QItemSelectionModel::Select);
    model->setData(index, text, Qt::DisplayRole);
}

void MainWindow::on_tableView_clicked(const QModelIndex &index)
{
    emit cellIndexChanged(index.row(), index.column());
}

void MainWindow::on_model_currentChanged(const QModelIndex &curr, const QModelIndex &prev)
{
    Q_UNUSED(prev);

    if (curr.isValid())
    {
        labelCellPos->setText(QString::asprintf("当前单元格: %d行, %d列", curr.row(), curr.column()));
        QStandardItem *item = model->itemFromIndex(curr);
        labelCellText->setText("单元格内容: " + item->text());
    }
}