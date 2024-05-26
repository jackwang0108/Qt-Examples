#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    // 在代码中重新设置名称
    ui->helloLabel->setText("你好，世界！");
    ui->closeButton->setText("关闭");

}

Widget::~Widget()
{
    delete ui;
}
