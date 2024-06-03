#include "widget.h"
#include "./ui_widget.h"

#include <QMessageBox>

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    grabKeyboard();
}

Widget::~Widget()
{
    delete ui;
}

void Widget::mousePressEvent(QMouseEvent *event)
{
    if (event->button() != Qt::LeftButton)
        return;

    // 相对于父组件的位置
    QPoint relativePos = event->pos();
    // 相对于根组件的位置
    QPointF absolutePos = event->position();
    // 相对于窗口的位置
    QPointF winPos = event->scenePosition();
    // 相对于屏幕的位置
    QPointF globalPos = event->globalPosition();

    QString str = QString::asprintf("pos()=(%d,%d)\n", relativePos.x(), relativePos.y());
    str += QString::asprintf("position()=(%.2f,%.2f)\n", absolutePos.x(), absolutePos.y());
    str += QString::asprintf("scenePosition()=(%.2f,%.2f)\n", winPos.x(), winPos.y());
    str += QString::asprintf("globalPosition()=(%.2f,%.2f)\n", globalPos.x(), globalPos.y());

    ui->labelClick->setText(str);
    ui->labelClick->adjustSize();
    ui->labelClick->move(event->pos());

    QWidget::mousePressEvent(event);
}

void Widget::keyPressEvent(QKeyEvent *event)
{
    QPoint btnPos = ui->btnClick->pos();

    int key = event->key();
    if (key == Qt::Key_A || key == Qt::Key_Left)
        btnPos.setX(btnPos.x() - 20);
    if (key == Qt::Key_D || key == Qt::Key_Right)
        btnPos.setX(btnPos.x() + 20);
    if (key == Qt::Key_S || key == Qt::Key_Down)
        btnPos.setY(btnPos.y() + 20);
    if (key == Qt::Key_W || key == Qt::Key_Up)
        btnPos.setY(btnPos.y() - 20);

    ui->btnClick->move(btnPos);

    QWidget ::keyPressEvent(event);
}

void Widget::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    painter.drawPixmap(0, 0, width(), this->height(), QPixmap(":/images/images/background.jpg"));
}

void Widget::closeEvent(QCloseEvent *event)
{
    QMessageBox::StandardButton result = QMessageBox::question(
        this,
        "确认",
        "是否关闭",
        QMessageBox::Yes | QMessageBox::No | QMessageBox::Cancel);

    if (result == QMessageBox::Yes)
        event->accept();
    else
        event->ignore();
}