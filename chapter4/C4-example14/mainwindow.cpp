#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    labelCellIndex = new QLabel("当前单元格坐标: ", this);
    labelCellIndex->setMinimumWidth(250);
    labelCellType = new QLabel("当前单元格类型: ", this);
    labelCellIndex->setMinimumWidth(200);
    labelStuID = new QLabel("学生ID: ", this);
    labelStuID->setMinimumWidth(200);

    ui->statusbar->addWidget(labelCellIndex);
    ui->statusbar->addWidget(labelCellType);
    ui->statusbar->addWidget(labelStuID);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnSetHHeader_clicked()
{
    ui->tableWidget->clear();

    QStringList headerText;
    headerText << "姓名"
               << "性别"
               << "出生日期"
               << "民族"
               << "是否为党员"
               << "分数";
    ui->tableWidget->setColumnCount(headerText.size());

    for (int i = 0; i < ui->tableWidget->columnCount(); i++)
    {
        QTableWidgetItem *headerItem = new QTableWidgetItem(headerText[i]);

        // 设置字体
        QFont font = headerItem->font();
        font.setBold(true);
        font.setPointSize(11);
        headerItem->setFont(font);
        headerItem->setForeground(QBrush(Qt::red));
        ui->tableWidget->setHorizontalHeaderItem(i, headerItem);
    }
}

void MainWindow::on_btnSetColumns_clicked()
{
    ui->tableWidget->setRowCount(ui->spinBox->value());
}

void MainWindow::on_btnTableInit_clicked()
{
    ui->tableWidget->clearContents();

    QDate birthday(2000, 2, 2);
    for (int i = 0; i < ui->tableWidget->rowCount(); i++)
    {
        QString strName = QString("学生%1").arg(i);
        QString strSex = i % 2 == 0 ? "男生" : "女生";
        bool isParty = i % 3 == 0 ? false : true;
        int score = QRandomGenerator::global()->bounded(60, 100);

        createTableRow(i, strName, strSex, birthday, "汉族", isParty, score);

        birthday = birthday.addDays(QRandomGenerator::global()->bounded(10, 30));
    }
}

void MainWindow::createTableRow(int rowIdx, QString name, QString sex, QDate birthday, QString nationality, bool isParty, int score)
{
    uint stuID = 20221000 + rowIdx;
    QTableWidgetItem *itemName = new QTableWidgetItem(name, ctName);
    itemName->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    itemName->setData(Qt::UserRole, QVariant(stuID));
    ui->tableWidget->setItem(rowIdx, colName, itemName);

    QTableWidgetItem *itemSex = new QTableWidgetItem(sex, ctSex);
    itemSex->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);

    QIcon icon;
    icon.addFile(sex == "男生" ? ":/images/icons/boy.ico" : ":/images/icons/girl.ico");
    itemSex->setIcon(icon);
    itemSex->setFlags(Qt::ItemIsSelectable | Qt::ItemIsEnabled);
    ui->tableWidget->setItem(rowIdx, colSex, itemSex);

    QTableWidgetItem *itemBirth = new QTableWidgetItem(birthday.toString("yyyy-MM-dd"), ctBirth);
    itemBirth->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    ui->tableWidget->setItem(rowIdx, colBirth, itemBirth);

    QTableWidgetItem *itemNationality = new QTableWidgetItem(nationality, ctNationality);
    itemNationality->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    ui->tableWidget->setItem(rowIdx, colNationality, itemNationality);

    QTableWidgetItem *itemParty = new QTableWidgetItem("党员");
    itemParty->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    itemParty->setFlags(Qt::ItemIsSelectable | Qt::ItemIsEnabled | Qt::ItemIsUserCheckable);
    itemParty->setCheckState(isParty ? Qt::Checked : Qt::Unchecked);
    itemParty->setBackground(QBrush(Qt::yellow));
    itemParty->setForeground(QBrush(isParty ? Qt::red : Qt::black));
    ui->tableWidget->setItem(rowIdx, colParty, itemParty);

    QTableWidgetItem *itemScore = new QTableWidgetItem(QString::number(score), ctScore);
    itemScore->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    ui->tableWidget->setItem(rowIdx, colScore, itemScore);
}

void MainWindow::on_btnTableInsert_clicked()
{
    int currRowIdx = ui->tableWidget->currentRow();
    ui->tableWidget->insertRow(currRowIdx);
    createTableRow(currRowIdx, "新学生", "男生", QDate::fromString("2000-1-1", "yyyy-M-d"), "汉族", false, 88);
}

void MainWindow::on_btnTableAppend_clicked()
{
    int lastRowIdx = ui->tableWidget->rowCount();
    ui->tableWidget->insertRow(lastRowIdx);
    createTableRow(lastRowIdx, "新学生", "女生", QDate::fromString("2000-1-1", "yyyy-M-d"), "汉族", true, 88);
}

void MainWindow::on_btnTableDelete_clicked()
{
    int currRowIdx = ui->tableWidget->currentRow();
    ui->tableWidget->removeRow(currRowIdx);
}

void MainWindow::on_btnAutoHeight_clicked()
{
    ui->tableWidget->resizeRowsToContents();
}

void MainWindow::on_btnAutoWidth_clicked()
{
    ui->tableWidget->resizeColumnsToContents();
}

void MainWindow::on_btnReadtoEdit_clicked()
{
    ui->plainTextEdit->clear();

    for (int rowIdx = 0; rowIdx < ui->tableWidget->rowCount(); rowIdx++)
    {
        QTableWidgetItem *item;
        QString str = QString::asprintf("第%d行: ", rowIdx + 1);

        for (int colIdx = 0; colIdx < ui->tableWidget->columnCount() - 1; colIdx++)
        {
            item = ui->tableWidget->item(rowIdx, colIdx);
            str += item->text() + " ";
        }

        item = ui->tableWidget->item(rowIdx, colParty);
        str += item->checkState() == Qt::Checked ? "党员" : "群众";

        ui->plainTextEdit->appendPlainText(str);
    }
}

void MainWindow::on_chkColorRow_clicked(bool checked)
{
    ui->tableWidget->setAlternatingRowColors(checked);
}

void MainWindow::on_chkTableEditable_clicked(bool checked)
{
    if (checked)
        ui->tableWidget->setEditTriggers(QAbstractItemView::DoubleClicked | QAbstractItemView::SelectedClicked);
    else
        ui->tableWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
}

void MainWindow::on_btnShowHHeader_clicked(bool checked)
{
    ui->tableWidget->horizontalHeader()->setVisible(checked);
}

void MainWindow::on_btnShowVHeader_clicked(bool checked)
{
    ui->tableWidget->verticalHeader()->setVisible(checked);
}

void MainWindow::on_radioRowSelect_clicked()
{
    ui->tableWidget->setSelectionBehavior(QAbstractItemView::SelectRows);
}

void MainWindow::on_radioCellSelect_clicked()
{
    ui->tableWidget->setSelectionBehavior(QAbstractItemView::SelectItems);
}

void MainWindow::on_tableWidget_currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn)
{
}
