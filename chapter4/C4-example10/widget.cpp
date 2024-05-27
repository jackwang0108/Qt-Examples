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

void Widget::on_btnClear_clicked()
{
    ui->plainTextEdit->clear();
}

void Widget::on_btnInitItems_clicked()
{
    ui->comboItems->clear();

    QIcon icon;
    icon.addFile(":/icons/icons/aim.ico");

    for (int i = 0; i < 20; i++)
        ui->comboItems->addItem(icon, QString("Item %1").arg(i));
}

void Widget::on_chkEditable_clicked(bool checked)
{
    ui->comboItems->setEditable(checked);
}

void Widget::on_btnClearItems_clicked()
{
    ui->comboItems->clear();
}

void Widget::on_btnInitCities_clicked()
{
    ui->comboCities->clear();

    QMap<QString, int> cityZone{
        {"北京", 10},
        {"沙河", 50},
        {"上海", 50},
        {"南昌", 90},
    };

    for (const auto &[key, value] : cityZone.asKeyValueRange())
        ui->comboCities->addItem(key, value);
}

void Widget::on_comboItems_currentTextChanged(const QString &arg1)
{
    ui->plainTextEdit->appendPlainText(arg1);
}

void Widget::on_comboCities_currentIndexChanged(int index)
{
    Q_UNUSED(index);

    QString str = ui->comboCities->currentText() + ui->comboCities->currentData().toString();

    ui->plainTextEdit->appendPlainText(str);
}
