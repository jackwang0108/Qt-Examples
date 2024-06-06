#include "tdialogsize.h"
#include "ui_tdialogsize.h"

TDialogSize::TDialogSize(QWidget *parent)
    : QDialog(parent), ui(new Ui::TDialogSize)
{
    ui->setupUi(this);
}

TDialogSize::~TDialogSize()
{
    delete ui;
}

void TDialogSize::setRowCol(int row, int col)
{
    ui->spinRowNum->setValue(row);
    ui->spinColNum->setValue(col);
}

int TDialogSize::rowCount()
{
    return ui->spinRowNum->value();
}

int TDialogSize::colCount()
{
    return ui->spinRowNum->value();
}