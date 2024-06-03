#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    ui->labelSingleClick->installEventFilter(this);
    ui->labelDoubleClick->installEventFilter(this);
}

Widget::~Widget()
{
    delete ui;
}

bool Widget::eventFilter(QObject *watched, QEvent *event)
{
    if (watched == ui->labelSingleClick)
    {
        if (event->type() == QEvent::Enter)
            ui->labelSingleClick->setStyleSheet("background-color:rgb(170,255,255);");
        else if (event->type() == QEvent::Leave)
        {
            ui->labelSingleClick->setText("单击我");
            ui->labelSingleClick->setStyleSheet("");
        }
        else if (event->type() == QEvent::MouseButtonPress)
            ui->labelSingleClick->setText("鼠标被按下了");
        else if (event->type() == QEvent::MouseButtonRelease)
            ui->labelSingleClick->setText("鼠标被松开了");
    }
    else if (watched == ui->labelDoubleClick)
    {
        if (event->type() == QEvent::Enter)
            ui->labelDoubleClick->setStyleSheet("background-color:rgb(85,255,12);");
        else if (event->type() == QEvent::Leave)
        {
            ui->labelDoubleClick->setText("双击我");
            ui->labelDoubleClick->setStyleSheet("");
        }
        else if (event->type() == QEvent::MouseButtonDblClick)
            ui->labelDoubleClick->setText("鼠标被双击了");
        else if (event->type() == QEvent::MouseButtonRelease)
            ui->labelDoubleClick->setText("鼠标被松开了");
    }

    return QWidget::eventFilter(watched, event);
}