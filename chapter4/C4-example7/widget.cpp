#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    this->connect(ui->dial, &QSlider::valueChanged, this, &Widget::do_valueChanged);
    this->connect(ui->horizontalSlider, &QSlider::valueChanged, this, &Widget::do_valueChanged);
    this->connect(ui->horizontalScrollBar, &QSlider::valueChanged, this, &Widget::do_valueChanged);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::do_valueChanged(int value)
{
    ui->progressBar->setValue(value);
}

void Widget::on_chkTextVisibility_clicked(bool checked)
{
    ui->progressBar->setTextVisible(checked);
}

void Widget::on_chkInvertAppearance_clicked(bool checked)
{
    ui->progressBar->setInvertedAppearance(checked);
}

void Widget::on_radioPercentage_clicked()
{
    ui->progressBar->setFormat("%p%");
}

void Widget::on_radioCurrentValue_clicked()
{
    ui->progressBar->setFormat("%v");
}
