#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // 直接将split作为central widget, 避免了再次嵌套
    setCentralWidget(ui->splitter);

    labelCurrFile = new QLabel("当前文件", this);
    labelCurrFile->setMinimumWidth(200);

    labelCellPos = new QLabel("当前单元格", this);
    labelCellPos->setMinimumWidth(200);

    labelCellText = new QLabel("单元格内容", this);
    labelCellText->setMinimumWidth(200);

    ui->statusbar->addWidget(labelCurrFile);
    ui->statusbar->addWidget(labelCellPos);
    ui->statusbar->addWidget(labelCellText);

    standardModel = new QStandardItemModel(2, fixedColumnCount, this);
    selectionModel = new QItemSelectionModel(standardModel);

    ui->tableView->setModel(standardModel);
    ui->tableView->setSelectionModel(selectionModel);
    ui->tableView->setSelectionMode(QAbstractItemView::ExtendedSelection);
    ui->tableView->setSelectionBehavior(QAbstractItemView::SelectItems);

    connect(selectionModel, &QItemSelectionModel::currentChanged, this, &MainWindow::do_currentSelectionChanged);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actOpen_triggered()
{
    QString currPath = QCoreApplication::applicationDirPath();
    QString filePath = QFileDialog::getOpenFileName(this, "选择要打卡的文件", currPath, "数据文件(*.txt);;所有文件(*.*)");

    if (filePath.isEmpty())
        return;

    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    QStringList fileContent;
    ui->plainTextEdit->clear();

    QTextStream fileStream(&file);
    while (!fileStream.atEnd())
    {
        QString str = fileStream.readLine();
        ui->plainTextEdit->appendPlainText(str);
        fileContent.append(str);
    }

    file.close();

    QFileInfo info(filePath);

    labelCurrFile->setText("当前文件: " + info.fileName());
    ui->actAppend->setEnabled(true);
    ui->actInsert->setEnabled(true);
    ui->actSave->setEnabled(true);
    ui->actDelete->setEnabled(true);

    initModelData(fileContent);
}

void MainWindow::initModelData(const QStringList &fileContent)
{
    int rowCount = fileContent.size();
    standardModel->setRowCount(rowCount - 1);

    QString header = fileContent[0];
    QStringList headerList = header.split(QRegularExpression(R"(\s+)"), Qt::SkipEmptyParts);
    standardModel->setHorizontalHeaderLabels(headerList);

    int colIdx = 0;
    QStandardItem *item;
    for (int rowIdx = 1; rowIdx < rowCount; rowIdx++)
    {
        QString lineText = fileContent[rowIdx];
        QStringList lineList = lineText.split(QRegularExpression(R"(\s+)"), Qt::SkipEmptyParts);

        for (colIdx = 0; colIdx < fixedColumnCount - 1; colIdx++)
        {
            item = new QStandardItem(lineList[colIdx]);
            standardModel->setItem(rowIdx - 1, colIdx, item);
        }

        // 最后一列
        item = new QStandardItem(headerList[colIdx]);
        item->setCheckable(true);
        item->setBackground(QBrush(Qt::yellow));
        item->setForeground(QBrush(Qt::black));
        if (lineList[colIdx] == "0")
            item->setCheckState(Qt::Unchecked);
        else
            item->setCheckState(Qt::Checked);
        standardModel->setItem(rowIdx - 1, colIdx, item);
    }
}

void MainWindow::on_actSave_triggered()
{
}

void MainWindow::on_actAppend_triggered()
{
    QList<QStandardItem *> itemList;

    for (int i = 0; i < standardModel->columnCount() - 1; i++)
        itemList << new QStandardItem("0");

    QString str = standardModel->headerData(standardModel->columnCount() - 1, Qt::Horizontal).toString();
    QStandardItem *item = new QStandardItem(str);
    item->setCheckable(true);
    item->setCheckState(Qt::Unchecked);
    item->setBackground(QBrush(Qt::yellow));
    item->setForeground(QBrush(Qt::black));
    itemList << item;

    standardModel->insertRow(standardModel->rowCount(), itemList);
    selectionModel->clear();
    selectionModel->setCurrentIndex(standardModel->index(standardModel->rowCount() - 1, 0), QItemSelectionModel::Select);
}

void MainWindow::on_actInsert_triggered()
{
    QList<QStandardItem *> itemList;

    for (int i = 0; i < standardModel->columnCount() - 1; i++)
        itemList << new QStandardItem("0");

    QString str = standardModel->headerData(standardModel->columnCount() - 1, Qt::Horizontal).toString();
    QStandardItem *item = new QStandardItem(str);
    item->setCheckable(true);
    item->setCheckState(Qt::Unchecked);
    item->setBackground(QBrush(Qt::yellow));
    item->setForeground(QBrush(Qt::black));
    itemList << item;

    QModelIndex currIndex = selectionModel->currentIndex();
    standardModel->insertRow(currIndex.row(), itemList);
    selectionModel->clear();
    selectionModel->setCurrentIndex(standardModel->index(currIndex.row(), 0), QItemSelectionModel::Select);
}

void MainWindow::on_actDelete_triggered()
{
    QModelIndex currIndex = selectionModel->currentIndex();

    if (currIndex.row() != standardModel->rowCount() - 1)
    {
        standardModel->removeRow(currIndex.row());
        selectionModel->setCurrentIndex(currIndex, QItemSelectionModel::Select);
    }
    else
        standardModel->removeRow(currIndex.row());
}

void MainWindow::on_actModelData_triggered()
{
    ui->plainTextEdit->clear();

    QString str;
    QStandardItem *item;
    for (int colIdx = 0; colIdx < standardModel->columnCount(); colIdx++)
    {
        item = standardModel->horizontalHeaderItem(colIdx);
        str += item->text() + "\t";
    }

    ui->plainTextEdit->appendPlainText(str);

    int colIdx = 0;
    for (int rowIdx = 0; rowIdx < standardModel->rowCount(); rowIdx++)
    {
        str.clear();

        for (colIdx = 0; colIdx < standardModel->columnCount() - 1; colIdx++)
        {
            item = standardModel->item(rowIdx, colIdx);
            str += item->text() + "\t";
        }

        item = standardModel->item(rowIdx, colIdx);
        if (item->checkState() == Qt::Checked)
            str += "是";
        else
            str += "否";

        ui->plainTextEdit->appendPlainText(str);
    }
}

void MainWindow::on_actAlignLeft_triggered()
{
    if (!selectionModel->hasSelection())
        return;

    QModelIndexList indexList = selectionModel->selectedIndexes();
    for (auto &index : indexList)
        standardModel->itemFromIndex(index)->setTextAlignment(Qt::AlignLeft);
}

void MainWindow::on_actAlignCenter_triggered()
{
    if (!selectionModel->hasSelection())
        return;

    QModelIndexList indexList = selectionModel->selectedIndexes();
    for (auto &index : indexList)
        standardModel->itemFromIndex(index)->setTextAlignment(Qt::AlignCenter);
}

void MainWindow::on_actAlignRight_triggered()
{
    if (!selectionModel->hasSelection())
        return;

    QModelIndexList indexList = selectionModel->selectedIndexes();
    for (auto &index : indexList)
        standardModel->itemFromIndex(index)->setTextAlignment(Qt::AlignRight);
}

void MainWindow::on_actFontBold_triggered(bool checked)
{
    if (!selectionModel->hasSelection())
        return;

    QModelIndexList indexList = selectionModel->selectedIndexes();
    for (auto &index : indexList)
    {
        QFont font = standardModel->itemFromIndex(index)->font();
        font.setBold(checked);
        standardModel->itemFromIndex(index)->setFont(font);
    }
}

void MainWindow::do_currentSelectionChanged(const QModelIndex &curr, const QModelIndex &prev)
{
    Q_UNUSED(prev);

    if (curr == prev || !curr.isValid())
        return;

    labelCellPos->setText(QString::asprintf("当前单元格: %d行, %d列", curr.row(), curr.column()));

    QStandardItem *item = standardModel->itemFromIndex(curr);
    labelCellText->setText("单元格内容: " + item->text());
    ui->actFontBold->setChecked(item->font().bold());
}
