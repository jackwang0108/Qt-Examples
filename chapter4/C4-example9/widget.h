#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

class QTimer;
class QElapsedTimer;

QT_BEGIN_NAMESPACE
namespace Ui
{
    class Widget;
}
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

private:
    // 软件定时器
    QTimer *m_timer;

    // 计时器
    QElapsedTimer *m_elapsedTimer;

private slots:
    void do_timer_timeout();

    void on_btnStart_clicked();
    void on_btnStop_clicked();
    void on_btnDynamic_clicked();

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
