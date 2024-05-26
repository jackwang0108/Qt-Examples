#include "widget.h"
#include "./ui_widget.h"

#include <QTime>
#include <QTimer>
#include <QElapsedTimer>

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    m_timer = new QTimer(this);
    m_timer->stop();
    m_timer->setTimerType(Qt::CoarseTimer);
    ui->btnCoarse->setChecked(true);
    connect(m_timer, &QTimer::timeout, this, &Widget::do_timer_timeout);

    m_elapsedTimer = new QElapsedTimer();
}

Widget::~Widget()
{
    delete ui;

    delete m_timer;
    delete m_elapsedTimer;
}

void Widget::do_timer_timeout()
{
    QApplication::beep();

    QTime currentTime = QTime::currentTime();
    ui->lcdHour->display(currentTime.hour());
    ui->lcdMin->display(currentTime.minute());
    ui->lcdSec->display(currentTime.second());

    if (m_timer->isSingleShot())
    {
        // 设置label
        qint64 timeMsec = m_elapsedTimer->elapsed();

        QString str = QString("流逝的时间 %1 毫秒").arg(timeMsec);
        ui->labelElapsed->setText(str);

        ui->btnStart->setEnabled(true);
        ui->radioOnce->setEnabled(true);
        ui->btnStop->setEnabled(false);
    }
}

void Widget::on_btnStart_clicked()
{
    m_timer->setInterval(ui->spinBox->value());
    m_timer->setSingleShot(ui->radioOnce->isChecked());

    if (ui->btnPrecise->isChecked())
        m_timer->setTimerType(Qt::PreciseTimer);
    else if (ui->btnCoarse->isChecked())
        m_timer->setTimerType(Qt::CoarseTimer);
    else
        m_timer->setTimerType(Qt::VeryCoarseTimer);

    m_timer->start();

    m_elapsedTimer->start();
    ui->btnStart->setEnabled(false);
    ui->btnStop->setEnabled(true);
    ui->radioOnce->setEnabled(true);
}

void Widget::on_btnStop_clicked()
{
    m_timer->stop();

    qint64 msec = m_elapsedTimer->elapsed();
    qint64 timeMSec = msec % 1000;
    qint64 timeSec = msec / 1000;
    QString str = QString("流逝的时间 %1 秒, %2 毫秒").arg(timeSec).arg(timeMSec);
    ui->labelElapsed->setText(str);

    ui->btnStart->setEnabled(true);
    ui->radioOnce->setEnabled(true);
    ui->btnStop->setEnabled(false);
}

void Widget::on_btnDynamic_clicked()
{
    int timeValue = ui->spinBox->value();

    QTimer::singleShot(timeValue, Qt::PreciseTimer, this, &Widget::do_timer_timeout);

    m_timer->setSingleShot(true);

    m_elapsedTimer->start();
    ui->radioOnce->setEnabled(false);
}
