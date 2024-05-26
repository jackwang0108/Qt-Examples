#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_btnCalTotal_clicked()
{
    int number = ui->editNum->text().toInt();

    float price = ui->editPrice->text().toFloat();

    float total = number * price;

    QString str = QString::number(total, 'f', 2);
    // str.setNum(total, 'f', 2);

    ui->editTotal->setText(str);
}

void Widget::on_btnTotal_clicked()
{
    qDebug("PI=%f", 3.1415926);

    QString str = QString::number(3.1415926, 'f', 10);
    qDebug("PI=%s", str.toLocal8Bit().data());
}

void Widget::on_btnDec_clicked()
{
    int value = ui->editDecimal->text().toInt();

    QString strHex = QString::number(value, 16);
    ui->editHex->setText(strHex);

    QString strBin = QString::number(value, 2);
    ui->editBinary->setText(strBin);
}

void Widget::on_btnBin_clicked()
{
    bool ok = false;
    int value = ui->editBinary->text().toInt(&ok, 2);

    if (!ok)
        return;

    QString strHex = QString::number(value, 16);
    ui->editHex->setText(strHex);

    QString strDec = QString::number(value, 10);
    ui->editDecimal->setText(strDec);
}

void Widget::on_btnHex_clicked()
{
    bool ok = false;
    int value = ui->editHex->text().toInt(&ok, 16);

    if (!ok)
        return;

    QString strDec = QString::number(value, 16);
    ui->editBinary->setText(strDec);

    QString strBin = QString::number(value, 2);
    ui->editBinary->setText(strBin);
}
