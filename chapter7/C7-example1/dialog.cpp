#include "dialog.h"
#include "./ui_dialog.h"

#include <QFont>
#include <QColor>
#include <QLineEdit>
#include <QFontDialog>
#include <QFileDialog>
#include <QMessageBox>
#include <QColorDialog>
#include <QInputDialog>
#include <QElapsedTimer>
#include <QProgressDialog>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent), ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_btnOpen_clicked()
{
    QString currPath = QCoreApplication::applicationDirPath();
    QString filePath = QFileDialog::getOpenFileName(this, "选择要打开的文件", currPath, "文本文件(*.txt);;图片(*.jpg *.gif *.png);;所有文件(*.*)");

    if (filePath.isEmpty())
        return;

    ui->plainTextEdit->appendPlainText(filePath);
}

void Dialog::on_btnOpenMulti_clicked()
{
    QString currPath = QCoreApplication::applicationDirPath();
    QStringList filePaths = QFileDialog::getOpenFileNames(this, "选择要打开的文件", currPath, "文本文件(*.txt);;图片(*.jpg *.gif *.png);;所有文件(*.*)");

    if (filePaths.empty())
        return;

    for (const QString &filePath : filePaths)
        ui->plainTextEdit->appendPlainText(filePath);
}

void Dialog::on_btnSelDir_clicked()
{
    QString currPath = QCoreApplication::applicationDirPath();
    QString dirPath = QFileDialog::getExistingDirectory(this, "选择文件夹", currPath);

    if (dirPath.isEmpty())
        return;

    ui->plainTextEdit->appendPlainText(dirPath);
}

void Dialog::on_btnSave_clicked()
{
    QString currPath = QCoreApplication::applicationDirPath();
    QString filePath = QFileDialog::getSaveFileName(this, "保存文件", currPath, "文本文件(*.txt);;图片(*.jpg *.gif *.png);;所有文件(*.*)");

    if (filePath.isEmpty())
        return;

    ui->plainTextEdit->appendPlainText(filePath);
}

void Dialog::on_btnColor_clicked()
{
    QPalette palette = ui->plainTextEdit->palette();
    QColor currColor = palette.color(QPalette::Text);
    QColor color = QColorDialog::getColor(currColor, this, "选择一个颜色");

    if (!color.isValid())
        return;

    palette.setColor(QPalette::Text, color);
    ui->plainTextEdit->setPalette(palette);
}

void Dialog::on_btnFont_clicked()
{
    // QFont font = ui->plainTextEdit->font();

    bool ok = false;
    QFont selectedFont = QFontDialog::getFont(&ok, this);

    if (!ok)
        return;

    ui->plainTextEdit->setFont(selectedFont);
}

void Dialog::on_btnProgress_clicked()
{
    int min = 0, max = 200;
    QProgressDialog dlgProgress("正在复制文件...", "取消", min, max, this);
    dlgProgress.setWindowTitle("复制文件");
    dlgProgress.setWindowModality(Qt::WindowModal);

    connect(&dlgProgress, &QProgressDialog::canceled, [&]
            { ui->plainTextEdit->appendPlainText("进度已取消"); });

    QElapsedTimer msCounter;
    for (int i = min; i <= max; i++)
    {
        dlgProgress.setValue(i);
        dlgProgress.setLabelText(QString::asprintf("正在复制文件, 第%d个", i));

        msCounter.start();
        while (true)
        {
            if (msCounter.elapsed() > 30)
                break;
        }

        if (dlgProgress.wasCanceled())
            break;
    }
}

void Dialog::on_btnMsgQuestion_clicked()
{
    QString title = "Question消息框";
    QString textLabel = "文件已被修改, 是否保存?";

    int result = QMessageBox::question(this, title, textLabel, QMessageBox::Yes | QMessageBox::No | QMessageBox::Cancel, QMessageBox::NoButton);

    QString str;
    if (result == QMessageBox::Yes)
        str = "文件已保存";
    else if (result == QMessageBox::No)
        str = "文件未保存";
    else
        str = "取消";
    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_btnMsgInformation_clicked()
{
    QString title = "Information消息框";
    QString textLabel = "文件已打开, 请检查";

    QMessageBox::information(this, title, textLabel);
}

void Dialog::on_btnMsgWarning_clicked()
{
    QString title = "Warning消息框";
    QString textLabel = "文件已被删除";

    QMessageBox::warning(this, title, textLabel);
}

void Dialog::on_btnMsgCritical_clicked()
{
    QString title = "Critical消息框";
    QString textLabel = "程序已经被删除";

    QMessageBox::critical(this, title, textLabel);
}

void Dialog::on_btnMsgAbout_clicked()
{
    QString title = "About消息框";
    QString textLabel = "Author: Jack Wang, Version: 1.0";

    QMessageBox::critical(this, title, textLabel);
}

void Dialog::on_btnMsgAboutQt_clicked()
{
    QMessageBox::aboutQt(this, "aboutQt消息框");
}

void Dialog::on_btnInputString_clicked()
{
    bool ok = false;
    QString title = "输入文字对话框";
    QString textLabel = "请输入文件名";
    QString initString = "新建文件.txt";
    QLineEdit::EchoMode echoMode = QLineEdit::Normal;
    // QLineEdit::EchoMode echoMode = QLineEdit::Password;
    QString text = QInputDialog::getText(this, title, textLabel, echoMode, initString, &ok);

    if (!ok || text.isEmpty())
        return;

    ui->plainTextEdit->appendPlainText(text);
}

void Dialog::on_btnInputInt_clicked()
{
    bool ok = false;
    QString title = "输入整数对话框";
    QString textLabel = "设置文本框字体大小";
    int min = 6;
    int max = 60;
    int step = 1;
    int defaultFontSize = ui->plainTextEdit->font().pointSize();
    int value = QInputDialog::getInt(this, title, textLabel, defaultFontSize, min, max, step, &ok);

    if (!ok)
        return;

    QString str = QString::asprintf("文本框字体大小被设置为%d", value);
    ui->plainTextEdit->appendPlainText(str);
    QFont f = ui->plainTextEdit->font();
    f.setPointSize(value);
    ui->plainTextEdit->setFont(f);
}

void Dialog::on_btnInputFloat_clicked()
{
    bool ok = false;
    QString title = "输入浮点数对话框";
    QString textLabel = "输入一个浮点数";
    float min = 0;
    float max = 10000;
    float defaultValue = 3.14;
    int decimals = 2;
    float value = QInputDialog::getDouble(this, title, textLabel, defaultValue, min, max, decimals, &ok);

    if (!ok)
        return;

    QString str = QString::asprintf("输入的浮点数为%f", value);
    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_btnInputItem_clicked()
{
    QStringList items{"优", "良", "中", "差"};
    QString title = "输入项对话框";
    QString textLabel = "选择一个级别";
    int currIndex = 0;
    bool editable = false;
    bool ok;

    QString text = QInputDialog::getItem(this, title, textLabel, items, currIndex, editable, &ok);

    if (!ok || text.isEmpty())
        return;

    ui->plainTextEdit->appendPlainText(text);
}
