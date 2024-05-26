#include "dialog.h"
#include "./ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent), ui(new Ui::Dialog)
{
    ui->setupUi(this);

    // 手动连接信号与槽
    connect(ui->radioButtonBlack, SIGNAL(clicked()), this, SLOT(do_fontColor()));
    connect(ui->radioButtonBlue, SIGNAL(clicked()), this, SLOT(do_fontColor()));
    connect(ui->radioButtonRed, SIGNAL(clicked()), this, SLOT(do_fontColor()));
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_pushButtonClear_clicked()
{
    ui->plainTextEdit->clear();
}

void Dialog::on_checkBoxlUnderline_clicked(bool checked)
{
    QFont font = ui->plainTextEdit->font();
    font.setUnderline(checked);
    ui->plainTextEdit->setFont(font);
}

void Dialog::on_checkBoxItalic_clicked(bool checked)
{
    QFont font = ui->plainTextEdit->font();
    font.setItalic(checked);
    ui->plainTextEdit->setFont(font);
}

void Dialog::on_checkBoxBold_clicked(bool checked)
{
    QFont font = ui->plainTextEdit->font();
    font.setBold(checked);
    ui->plainTextEdit->setFont(font);
}

void Dialog::do_fontColor()
{
    QPalette palet = ui->plainTextEdit->palette();

    if (ui->radioButtonBlack->isChecked())
        palet.setColor(QPalette::Text, Qt::black);
    if (ui->radioButtonBlue->isChecked())
        palet.setColor(QPalette::Text, Qt::blue);
    if (ui->radioButtonRed->isChecked())
        palet.setColor(QPalette::Text, Qt::red);

    ui->plainTextEdit->setPalette(palet);
}
