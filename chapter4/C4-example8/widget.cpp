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

void Widget::on_pushButton_clicked()
{
    QDateTime currDataTime = QDateTime::currentDateTime();

    // set time
    ui->timeEdit->setTime(currDataTime.time());
    ui->timeLineEdit->setText(currDataTime.toString("hh:mm:ss"));

    // set date
    ui->dateEdit->setDate(currDataTime.date());
    ui->dateLineEdit->setText(currDataTime.toString("yyyy-MM-dd"));

    // set date time
    ui->dateTimeEdit->setDateTime(currDataTime);
    ui->dateTimeLineEdit->setText(currDataTime.toString("yyyy-MM-dd hh:mm:ss"));
}

void Widget::on_qDebugTime_clicked()
{
    QTime time1(13, 24, 5);
    QString strTime1 = time1.toString("HH:mm:ss");
    qDebug("Original Time=%s", strTime1.toLocal8Bit().data());

    QTime time2 = time1.addSecs(150);
    QString strTime2 = time2.toString("HH:mm:ss");
    qDebug("150s later Time=%s", strTime2.toLocal8Bit().data());

    QTime time3 = QTime::currentTime();
    QString strTime3 = time3.toString("HH:mm:ss zzz");
    qDebug("Current Time=%s", strTime3.toLocal8Bit().data());
    qDebug("Hour=%d", time3.hour());
    qDebug("Minute=%d", time3.minute());
    qDebug("Second=%d", time3.second());
    qDebug("MillSecond=%d", time3.msec());
}

void Widget::on_qDebugDate_clicked()
{
    QDate date1(2024, 10, 10);
    QString date1Str = date1.toString("yyyy-MM-dd");
    qDebug("Date1 = %s", date1Str.toLocal8Bit().data());

    QDate date2;
    date2.setDate(2021, 8, 25);
    QString date2Str = date2.toString("yyyy-MM-dd");
    qDebug("Date2 = %s", date2Str.toLocal8Bit().data());
    qDebug("Days between date2 and date1 is %lld", date2.daysTo(date1));

    QDate date3 = QDate::currentDate();
    QString date3Str = date3.toString("yyyy-MM-dd");
    qDebug("Current date = %s", date3Str.toLocal8Bit().data());
    qDebug("Year = %d", date3.year());
    qDebug("Month = %d", date3.month());
    qDebug("Day = %d", date3.day());
    qDebug("Day of week = %d", date3.dayOfWeek());
    qDebug("Day of year = %d", date3.dayOfYear());
    qDebug("Days in month = %d", date3.daysInMonth());
    qDebug("Days in year = %d", date3.daysInYear());
}

void Widget::on_qDebugDateTime_clicked()
{
    QDateTime dateTime = QDateTime::currentDateTime();
    QString str = dateTime.toString("yyyy-MM-dd hh:mm:ss");
    qDebug("dateTime1 = %s", str.toLocal8Bit().data());

    QDate date = dateTime.date();
    str = date.toString("yyyy-MM-dd");
    qDebug("dateTime1.date() = %s", str.toLocal8Bit().data());

    QTime time = dateTime.time();
    str = time.toString("hh:mm:ss zzz");
    qDebug("datetime1.time() = %s", str.toLocal8Bit().data());

    // 转换为Unix时间戳
    qint64 ms = dateTime.toSecsSinceEpoch();
    qDebug("dateTime1.toSecsSinceEpoch() = %lld", ms);

    // 加120秒
    ms += 120;
    dateTime.setSecsSinceEpoch(ms);
    str = dateTime.toString("yyyy-MM-dd hh:mm:ss");
    qDebug("dateTime1 + 120s = %s", str.toLocal8Bit().data());
}

void Widget::on_btnSetTime_clicked()
{
    QString strTime = (ui->timeLineEdit->text()).trimmed();

    if (!strTime.isEmpty())
    {
        QTime time = QTime::fromString(strTime, "hh:mm:ss");
        ui->timeEdit->setTime(time);
    }
}

void Widget::on_btnSetDate_clicked()
{
    QString strDate = (ui->dateLineEdit->text()).trimmed();

    if (!strDate.isEmpty())
    {
        QDate date = QDate::fromString(strDate, "yyyy-MM-dd");
        ui->dateEdit->setDate(date);
    }
}

void Widget::on_btnSetDateTime_clicked()
{
    QString strDateTime = (ui->dateTimeLineEdit->text()).trimmed();

    if (!strDateTime.isEmpty())
    {
        QDateTime dateTime = QDateTime::fromString(strDateTime, "yyyy-MM-dd hh:mm:ss");
        ui->dateTimeEdit->setDateTime(dateTime);
    }
}

void Widget::on_calendarWidget_selectionChanged()
{
    QString str = ui->calendarWidget->selectedDate().toString("yyyy年MM月dd日");
    ui->lineEdit->setText(str);
}
