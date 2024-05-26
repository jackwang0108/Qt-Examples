#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    on_btnFontBold_clicked(ui->btnFontBold->isChecked());
    on_btnFontItalic_clicked(ui->btnFontItalic->isChecked());
    on_btnFontUnderline_clicked(ui->btnFontUnderline->isChecked());
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_btnAlignLeft_clicked()
{
    ui->lineEdit->setAlignment(Qt::AlignLeft);
}

void Widget::on_btnAlignCenter_clicked()
{
    ui->lineEdit->setAlignment(Qt::AlignCenter);
}

void Widget::on_btnAlignRight_clicked()
{
    ui->lineEdit->setAlignment(Qt::AlignRight);
}

void Widget::on_btnFontBold_clicked(bool checked)
{
    QFont font = ui->lineEdit->font();
    font.setBold(checked);
    ui->lineEdit->setFont(font);
}

void Widget::on_btnFontItalic_clicked(bool checked)
{
    QFont font = ui->lineEdit->font();
    font.setItalic(checked);
    ui->lineEdit->setFont(font);
}

void Widget::on_btnFontUnderline_clicked(bool checked)
{
    QFont font = ui->lineEdit->font();
    font.setUnderline(checked);
    ui->lineEdit->setFont(font);
}

void Widget::on_checkReadOnly_clicked(bool checked)
{
    ui->lineEdit->setReadOnly(checked);
}

void Widget::on_checkEnabled_clicked(bool checked)
{
    ui->lineEdit->setEnabled(checked);
}

void Widget::on_checkClearEnabled_clicked(bool checked)
{
    ui->lineEdit->setClearButtonEnabled(checked);
}

void Widget::on_radioBlack_clicked()
{
    QPalette palette = ui->lineEdit->palette();
    palette.setColor(QPalette::Text, Qt::black);
    ui->lineEdit->setPalette(palette);
}

void Widget::on_radioRed_clicked()
{
    QPalette palette = ui->lineEdit->palette();
    palette.setColor(QPalette::Text, Qt::red);
    ui->lineEdit->setPalette(palette);
}

void Widget::on_radioBlue_clicked()
{
    QPalette palette = ui->lineEdit->palette();
    palette.setColor(QPalette::Text, Qt::blue);
    ui->lineEdit->setPalette(palette);
}
