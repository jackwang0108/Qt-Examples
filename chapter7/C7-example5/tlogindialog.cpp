#include "tlogindialog.h"
#include "ui_tlogindialog.h"

#include <QSettings>
#include <QMessageBox>
#include <QMouseEvent>
#include <QCryptographicHash>

QString TLoginDialog::encrypt(const QString &str)
{
    QCryptographicHash hash{QCryptographicHash::Md5};
    hash.addData(str.toLocal8Bit());
    return hash.result().toHex();
}

void TLoginDialog::readSettings()
{
    QSettings setting;

    bool saved = setting.value("Saved", false).toBool();
    user = setting.value("Username", "user").toString();
    pass = setting.value("Password", encrypt("12345")).toString();
    // pass = encrypted("12345");

    if (saved)
        ui->lineEditUserName->setText(user);
    ui->checkBox->setChecked(saved);
}

void TLoginDialog::writeSettings()
{
    QSettings setting;
    setting.setValue("Username", user);
    setting.setValue("Password", pass);
    setting.setValue("Saved", ui->checkBox->isChecked());
}

TLoginDialog::TLoginDialog(QWidget *parent)
    : QDialog(parent), ui(new Ui::TLoginDialog)
{
    ui->setupUi(this);
    setAttribute(Qt::WA_DeleteOnClose);

    // 会导致窗口无法拖动, 需要定义拖拽事件
    // setWindowFlag(Qt::SplashScreen);
    setWindowFlag(Qt::FramelessWindowHint);

    QApplication::setOrganizationName("JackWang");
    QApplication::setApplicationName("C7-example5");
    readSettings();
}

TLoginDialog::~TLoginDialog()
{
    delete ui;
}

void TLoginDialog::mousePressEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton)
    {
        moving = true;
        lastPosition = event->globalPosition().toPoint() - this->pos();
    }

    return QDialog::mousePressEvent(event);
}

void TLoginDialog::mouseReleaseEvent(QMouseEvent *event)
{
    moving = false;
    event->accept();
    return QDialog::mouseReleaseEvent(event);
}

void TLoginDialog::mouseMoveEvent(QMouseEvent *event)
{
    QPoint eventPosition = event->globalPosition().toPoint();
    if (
        moving &&
        (event->buttons() & Qt::LeftButton) &&
        (eventPosition - lastPosition - pos()).manhattanLength() > QApplication::startDragDistance())
    {
        move(eventPosition - lastPosition);
        lastPosition = eventPosition - pos();
    }

    return QDialog::mouseMoveEvent(event);
}

void TLoginDialog::on_btnOk_clicked()
{
    QString in_user = ui->lineEditUserName->text().trimmed();
    QString in_pass = ui->lineEditUserPass->text().trimmed();
    QString encryptedPass = encrypt(in_pass);

    if ((in_user == user) && (encryptedPass == pass))
    {
        writeSettings();
        this->accept();
    }
    else
    {
        if (++currTryTimes >= maxTryTimes)
        {
            QMessageBox::critical(this, "错误", "用户名或密码错误次数太多!");
            this->reject();
        }
        else
            QMessageBox::critical(this, "错误", "用户名或密码错误");
    }
}
