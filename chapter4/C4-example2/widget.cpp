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

void Widget::on_btnGetChars_clicked()
{
    QString str = ui->editStr->text();

    if (str.isEmpty())
        return;

    for (qsizetype i = 0; i < str.length(); i++)
    {
        QChar chr = str.at(i);

        char16_t uniCode = chr.unicode();

        QString chStr(chr);
        QString info = chStr + QString::asprintf("\t, UniCode编码=0x%X", uniCode);

        ui->plainTextEdit->appendPlainText(info);
    }
}

void Widget::on_btnClear_clicked()
{
    ui->plainTextEdit->clear();
}

void Widget::on_btnCharJudge_clicked()
{
    QString str = ui->editChar->text();

    if (str.isEmpty())
        return;

    QChar chr = str.at(0);
    char16_t uniCode = chr.unicode();

    QString info = chr + QString::asprintf("\t, UniCode编码=0x%X", uniCode);

    ui->plainTextEdit->appendPlainText(info);

    // 设置复选框
    ui->chkDigit->setChecked(chr.isDigit());
    ui->chkLetter->setChecked(chr.isLetter());
    ui->chkLetterOrNumber->setChecked(chr.isLetterOrNumber());
    ui->chkUpper->setChecked(chr.isUpper());
    ui->chkLowe->setChecked(chr.isLower());
    ui->chkMark->setChecked(chr.isMark());
    ui->chkSpace->setChecked(chr.isSpace());
    ui->chkSymbol->setChecked(chr.isSymbol());
    ui->chkPunct->setChecked(chr.isPunct());
}

void Widget::on_btnLatin1_clicked()
{
    QString str = "Dimple\n";
    ui->plainTextEdit->appendPlainText(str);

    QChar chP = QChar::fromLatin1('P');

    // C++的ascii char支持Latin1, 所以也可以直接写成
    // str[0] = 'P';
    str[0] = chP;

    ui->plainTextEdit->appendPlainText(str);
}

void Widget::on_btnUTF16_clicked()
{
    // Qt的QString内部将字符表示为Unicode, 所以可以直接输出中文
    QString str = "Hello, 北京\n";
    ui->plainTextEdit->appendPlainText(str);

    QChar chP = QChar::fromLatin1('P');

    // C++的ascii char不支持Unicode, 所以不能写成
    // str[7] = '青';
    str[7] = QChar::fromUcs2(0x9752);
    str[8] = QChar::fromUcs2(0x5C9B);

    // unicode编码需要查询, 所以更常见的是直接写字符串
    QString qingdao = "青岛";
    str[7] = qingdao[0];
    str[8] = qingdao[1];

    ui->plainTextEdit->appendPlainText(str);
}

void Widget::on_btnCompare_clicked()
{
    QString HuStr = "河to湖";

    QChar He = QChar::fromUcs2(HuStr[0].unicode());
    QChar Hu = QChar(HuStr[3].unicode());

    QString str = "他们来自河南或者河北\n";
    ui->plainTextEdit->appendPlainText(str);

    // Qt的QString内部将字符表示为Unicode, 取值和比较都是针对整个Unicode字符
    for (int i = 0; i < str.size(); i++)
        if (str.at(i) == He)
            str[i] = Hu;

    ui->plainTextEdit->appendPlainText(str);
}
