#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include <QFileDialog>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    model = new QFileSystemModel(this);
    ui->treeView->setModel(model);
    ui->listView->setModel(model);
    ui->tableView->setModel(model);

    ui->treeView->setRootIndex(model->index(QDir::currentPath()));
    model->setRootPath("");
    connect(ui->treeView, &QTreeView::clicked, ui->listView, &QListView::setRootIndex);
    connect(ui->treeView, &QTreeView::clicked, ui->tableView, &QTableView::setRootIndex);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actSetRootFolder_triggered()
{
    QString dir = QFileDialog::getExistingDirectory(this, "选择文件或目录", QDir::currentPath());
    if (dir.isEmpty())
        return;
    ui->treeView->setRootIndex(model->index(dir));
    ui->listView->setRootIndex(model->index(dir));
    ui->tableView->setRootIndex(model->index(dir));
}

void MainWindow::on_radioFolderFile_clicked(bool checked)
{
    model->setFilter(QDir::AllDirs | QDir::Files | QDir::NoDotAndDotDot);

    ui->groupFilter->setEnabled(true);
}

void MainWindow::on_radioFolderOnly_clicked(bool checked)
{
    model->setFilter(QDir::AllDirs | QDir::NoDotAndDotDot);
    ui->groupFilter->setEnabled(false);
}

void MainWindow::on_chkEnableFilter_clicked(bool checked)
{
    ui->comboFilter->setEnabled(checked);
    ui->btnApplyFilter->setEnabled(checked);
    model->setNameFilterDisables(!checked);
}

void MainWindow::on_comboFilter_currentIndexChanged(int index)
{
}

void MainWindow::on_btnApplyFilter_clicked()
{
    QStringList list = ui->comboFilter->currentText().trimmed().split(";", Qt::SkipEmptyParts);
    model->setNameFilters(list);
}

void MainWindow::on_treeView_clicked(const QModelIndex &index)
{
    ui->labelFileName->setText("文件名: " + model->fileName(index));
    ui->labelFilePath->setText("文件路径: " + model->filePath(index));
    ui->labelNodeType->setText("节点类型: " + model->type(index));
    ui->chkIsDir->setChecked(model->isDir(index));

    QString str = "文件大小: ";
    float size = model->size(index) / 1024.;
    if (size < 1024)
        str += QString::asprintf("%.1f KB", size);
    else
        str += QString::asprintf("%.1f MB", size / 1024.);

    ui->labelFileSize->setText(str);
}
