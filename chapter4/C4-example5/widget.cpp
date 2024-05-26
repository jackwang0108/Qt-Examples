#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    // 初始值设置
    this->on_btnCalculate_clicked();

    // spinBox的增减
    this->connect(ui->spinNum, &QSpinBox::valueChanged, this, &Widget::on_btnCalculate_clicked);
    this->connect(ui->spinPrice, &QSpinBox::valueChanged, this, &Widget::on_btnCalculate_clicked);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_btnCalculate_clicked()
{
    int num = ui->spinNum->value();
    int price = ui->spinPrice->value();

    int total = num * price;

    ui->spinTotal->setValue(total);
}

void Widget::on_spinBin_valueChanged(int value)
{
    ui->spinDec->setValue(value);
    ui->spinHex->setValue(value);
}

void Widget::on_spinDec_valueChanged(int value)
{
    ui->spinBin->setValue(value);
    ui->spinHex->setValue(value);
}

void Widget::on_spinHex_valueChanged(int value)
{

    ui->spinDec->setValue(value);
}
