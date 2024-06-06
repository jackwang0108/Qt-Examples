#include "tdialoglocate.h"
#include "ui_tdialoglocate.h"

TDialogLocate::TDialogLocate(QWidget *parent)
    : QDialog(parent), ui(new Ui::TDialogLocate)
{
    ui->setupUi(this);
}

TDialogLocate::~TDialogLocate()
{
    delete ui;
}

void TDialogLocate::on_btnOk_clicked()
{
    QString text = ui->lineEdit->text();
    int row = ui->spinRow->value();
    int col = ui->spinCol->value();

    if (ui->chkRowInc->isChecked())
        ui->spinRow->setValue(row + 1);

    if (ui->chkColInc->isChecked())
        ui->spinCol->setValue(col + 1);

    emit cellTextChanged(row, col, text);
}

void TDialogLocate::setSpinRange(int rowNum, int colNum)
{
    ui->spinCol->setMaximum(colNum - 1);
    ui->spinRow->setMaximum(rowNum - 1);
}

void TDialogLocate::setSpinValue(int row, int col)
{
    ui->spinRow->setValue(row);
    ui->spinCol->setValue(col);
}

void TDialogLocate::closeEvent(QCloseEvent *event)
{
    event->accept();
    emit changeActionEnabled(true);
}

void TDialogLocate::showEvent(QShowEvent *event)
{
    event->accept();
    emit changeActionEnabled(false);
}