#include "dialog.h"

#include <QHBoxLayout>
#include <QVBoxLayout>

void Dialog::do_chkBoxUnder(bool checked)
{
    QFont font = txtEdit->font();
    font.setUnderline(checked);
    txtEdit->setFont(font);
}

void Dialog::do_chkBoxBold(bool checked)
{
    QFont font = txtEdit->font();
    font.setBold(checked);
    txtEdit->setFont(font);
}

void Dialog::do_chkBoxItalic(bool checked)
{
    QFont font = txtEdit->font();
    font.setItalic(checked);
    txtEdit->setFont(font);
}

void Dialog::do_setFontColor()
{
    QPalette palette = txtEdit->palette();

    if (radioRed->isChecked())
        palette.setColor(QPalette::Text, Qt::red);
    if (radioBlue->isChecked())
        palette.setColor(QPalette::Text, Qt::blue);
    if (radioBlack->isChecked())
        palette.setColor(QPalette::Text, Qt::black);

    txtEdit->setPalette(palette);
}

void Dialog::do_clearTxtEdit()
{
    txtEdit->clear();
}

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
{
    // 复选框
    chkBoxBold = new QCheckBox("粗体");
    chkBoxItalic = new QCheckBox("斜体");
    chkBoxUnder = new QCheckBox("下划线");

    QHBoxLayout * Hlt1 = new QHBoxLayout();
    Hlt1->addWidget(chkBoxBold);
    Hlt1->addWidget(chkBoxUnder);
    Hlt1->addWidget(chkBoxItalic);

    // 单选框
    radioRed = new QRadioButton("红色");
    radioBlue = new QRadioButton("蓝色");
    radioBlack = new QRadioButton("黑色");

    QHBoxLayout * Hlt2 = new QHBoxLayout();
    Hlt2->addWidget(radioRed);
    Hlt2->addWidget(radioBlue);
    Hlt2->addWidget(radioBlack);

    // 输入框
    txtEdit = new QPlainTextEdit;
    txtEdit->setPlainText("你好，世界！");
    QFont font = txtEdit->font();
    font.setPixelSize(20);
    txtEdit->setFont(font);

    // 按钮
    btnOk = new QPushButton("确认");
    btnCancel = new QPushButton("清除");
    btnClose = new QPushButton("退出");

    QHBoxLayout * Hlt3 = new QHBoxLayout();
    Hlt3->addStretch();
    Hlt3->addWidget(btnCancel);
    Hlt3->addStretch();
    Hlt3->addWidget(btnOk);
    Hlt3->addWidget(btnClose);


    // 设置版面
    QVBoxLayout * Vlt = new QVBoxLayout();
    Vlt->addLayout(Hlt1);
    Vlt->addLayout(Hlt2);
    Vlt->addWidget(txtEdit);
    Vlt->addLayout(Hlt3);
    setLayout(Vlt);

    connect(chkBoxUnder, SIGNAL(clicked(bool)), this, SLOT(do_chkBoxUnder(bool)));
    connect(chkBoxBold, SIGNAL(clicked(bool)), this, SLOT(do_chkBoxBold(bool)));
    connect(chkBoxItalic, SIGNAL(clicked(bool)), this, SLOT(do_chkBoxItalic(bool)));

    connect(radioBlack, SIGNAL(clicked(bool)), this, SLOT(do_setFontColor()));
    connect(radioBlue, SIGNAL(clicked(bool)), this, SLOT(do_setFontColor()));
    connect(radioRed, SIGNAL(clicked(bool)), this, SLOT(do_setFontColor()));

    connect(btnOk, SIGNAL(clicked()), this, SLOT(accept()));
    connect(btnClose, SIGNAL(clicked()), this, SLOT(reject()));
    connect(btnCancel, SIGNAL(clicked()), this, SLOT(do_clearTxtEdit()));

    setWindowTitle("手工打造的UI");
}

Dialog::~Dialog() {}
