#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    setAcceptDrops(true);
    ui->label->setAcceptDrops(false);
    ui->label->setScaledContents(true);
    ui->plainTextEdit->setAcceptDrops(false);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::resizeEvent(QResizeEvent *event)
{
    QSize size = ui->plainTextEdit->size();
    ui->plainTextEdit->move(5, 5);
    ui->plainTextEdit->resize(this->width() - 10, size.height());
    ui->label->move(5, size.height() + 5);
    ui->label->resize(this->width() - 10, this->height() - size.height() - 20);
    event->accept();
}

void Widget::dragEnterEvent(QDragEnterEvent *event)
{
    ui->plainTextEdit->clear();
    ui->plainTextEdit->appendPlainText("dargEvent事件, mimeData类型: ");
    for (const auto &item : event->mimeData()->formats())
    {
        ui->plainTextEdit->appendPlainText(item);
    }

    ui->plainTextEdit->appendPlainText("dargEvent事件, mimeData url: ");
    for (const auto &item : event->mimeData()->urls())
    {
        ui->plainTextEdit->appendPlainText(item.toString());
    }

    if (event->mimeData()->hasUrls())
    {
        QString fileName = event->mimeData()->urls()[0].fileName();

        QFileInfo fileInfo(fileName);

        QString suffix = fileInfo.suffix().toUpper();
        if (suffix == "JPG")
            // 接受该动作, 即允许拖入
            event->acceptProposedAction();
        else
            event->ignore();
    }
    else
        event->ignore();
}

void Widget::dropEvent(QDropEvent *event)
{
    QUrl filePath = event->mimeData()->urls()[0];

    if (filePath.isLocalFile())
        filePath = filePath.toLocalFile();

    QPixmap pixmap(filePath.toString());
    ui->label->setPixmap(pixmap);
    event->accept();
}