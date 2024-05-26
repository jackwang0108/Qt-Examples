#include "widget.h"
#include "./ui_widget.h"
#include <string>

using namespace std::string_literals;

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

void Widget::on_btnFrontBack_clicked()
{
    ui->plainTextEdit->appendPlainText("Front&Back方法测试");
    QString str = ui->comboBoxPath->currentText();

    ui->plainTextEdit->appendPlainText(str);
    ui->plainTextEdit->appendPlainText("front=" + QString(str.front()));
    ui->plainTextEdit->appendPlainText("back=" + QString(str.back()));
}

void Widget::on_btnLeftRight_clicked()
{
    ui->plainTextEdit->appendPlainText("Left&Right方法测试");
    QString str = ui->comboBoxPath->currentText();

    ui->plainTextEdit->appendPlainText(str);
    ui->plainTextEdit->appendPlainText("left=" + QString(str.left(6)));
    ui->plainTextEdit->appendPlainText("right=" + QString(str.right(11)));
}

void Widget::on_btnFirstLast_clicked()
{
    ui->plainTextEdit->appendPlainText("First&Last方法测试");

    QString path = ui->comboBoxPath->currentText();
    QString delim = ui->comboBoxDelim->currentText();

    ui->plainTextEdit->appendPlainText("Path=" + path);
    ui->plainTextEdit->appendPlainText("Delim=" + delim);

    int index = path.lastIndexOf(delim);

    ui->plainTextEdit->appendPlainText("路径名称=" + path.first(index + 1));
    ui->plainTextEdit->appendPlainText("文件名称=" + path.last(path.size() - index - 1));
}

void Widget::on_btnSection_clicked()
{
    ui->plainTextEdit->appendPlainText("Section方法测试");

    QString path = ui->comboBoxPath->currentText();
    QString delim = ui->comboBoxDelim->currentText();

    int N = ui->spinBox->value();

    QString strSection = path.section(delim, N, N);
    ui->plainTextEdit->appendPlainText(strSection);
}

void Widget::on_btnIsNullIsEmpty_clicked()
{
    ui->plainTextEdit->appendPlainText("isNull和isEmpty函数测试");

    QString str1, str2 = "";
    ui->plainTextEdit->appendPlainText("QString str1, str2=\"");

    QString str = "str1.isNull()=";
    if (str1.isNull())
        str += "true";
    else
        str += "false";
    ui->plainTextEdit->appendPlainText(str);

    str = "str1.isEmpty()=";
    if (str1.isEmpty())
        str += "true";
    else
        str += "false";
    ui->plainTextEdit->appendPlainText(str);

    str = "str2.isNull()=";
    if (str2.isNull())
        str += "true";
    else
        str += "false";
    ui->plainTextEdit->appendPlainText(str);

    str = "str2.isEmpty()=";
    if (str1.isEmpty())
        str += "true";
    else
        str += "false";
    ui->plainTextEdit->appendPlainText(str);
}

void Widget::on_btnResize_clicked()
{
    ui->plainTextEdit->appendPlainText("resize函数测试:");

    QString str;
    str.resize(5, '0');
    ui->plainTextEdit->appendPlainText("str=" + str);

    str.resize(10, QChar(0x54C8));
    ui->plainTextEdit->appendPlainText("str=" + str);
}

void Widget::on_btnSizeLength_clicked()
{
    ui->plainTextEdit->appendPlainText("size&count&length函数测试:");

    QString str = ui->comboBoxPath->currentText();

    ui->plainTextEdit->appendPlainText(str);

    ui->plainTextEdit->appendPlainText(QString::asprintf("str.size()=%lld", str.size()));
    ui->plainTextEdit->appendPlainText(QString::asprintf("str.count()=%lld", str.count()));
    ui->plainTextEdit->appendPlainText(QString::asprintf("str.length()=%lld", str.length()));
}

void Widget::on_btnFill_clicked()
{
    ui->plainTextEdit->appendPlainText("fill函数测试:");

    QString str = "Hello";
    ui->plainTextEdit->appendPlainText("str=" + str);

    str.fill('X');
    ui->plainTextEdit->appendPlainText("str=" + str);

    str.fill('A', 2);
    ui->plainTextEdit->appendPlainText("str=" + str);

    auto ha = u'哈';
    str.fill(ha, 3);
    ui->plainTextEdit->appendPlainText("str=" + str);
}

void Widget::on_btnTrimmedSimplified_clicked()
{
    ui->plainTextEdit->appendPlainText("trim&simplified函数测试:");

    QString str = ui->comboBoxPath->currentText();

    ui->plainTextEdit->appendPlainText("str=" + str);

    ui->plainTextEdit->appendPlainText("str.trimmed()=" + str.trimmed());

    ui->plainTextEdit->appendPlainText("str.simplified()=" + str.simplified());
}

void Widget::on_btnInsert_clicked()
{
    ui->plainTextEdit->appendPlainText("insert函数测试:");

    QString str1 = "It is great";
    ui->plainTextEdit->appendPlainText(str1);

    int N = str1.lastIndexOf(" ");
    str1.insert(N, "n't");

    ui->plainTextEdit->appendPlainText(str1);
}

void Widget::on_btnRemove_clicked()
{
    ui->plainTextEdit->appendPlainText("remove函数测试:");

    ui->plainTextEdit->appendPlainText("删除指定字符");
    QString str1 = "你们, 我们, 他们";
    ui->plainTextEdit->appendPlainText(str1);

    QString deleteStr = "们";
    QChar deleteChar = QChar(deleteStr[0].unicode());
    str1.remove(deleteChar);
    ui->plainTextEdit->appendPlainText(str1);

    ui->plainTextEdit->appendPlainText("删除右侧N个字符");
    str1 = ui->comboBoxPath->currentText();
    ui->plainTextEdit->appendPlainText(str1);

    int N = str1.lastIndexOf("/");
    str1.remove(N + 1, 20);
    ui->plainTextEdit->appendPlainText(str1);
}

void Widget::on_btnReplaced_clicked()
{
    ui->plainTextEdit->appendPlainText("replace函数测试:");

    QString str = "Gooooogle";
    ui->plainTextEdit->appendPlainText(str);

    str.replace('o', 'e');
    ui->plainTextEdit->appendPlainText(str);

    ui->plainTextEdit->appendPlainText("replace替换字符串");
    str = "It is great";
    int N = str.lastIndexOf(" ");
    ui->plainTextEdit->appendPlainText(str);
    QString subStr = "wonderful";
    str.replace(N + 1, subStr.size(), subStr);
    ui->plainTextEdit->appendPlainText(str);

    str.replace(N + 1, subStr.size(), "OK!");
    qDebug(str.toLocal8Bit().data());
    ui->plainTextEdit->appendPlainText(str);
}
