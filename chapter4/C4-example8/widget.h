#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui
{
    class Widget;
}
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_pushButton_clicked();

    void on_qDebugTime_clicked();
    void on_qDebugDate_clicked();
    void on_qDebugDateTime_clicked();

    void on_btnSetTime_clicked();
    void on_btnSetDate_clicked();
    void on_btnSetDateTime_clicked();

    void on_calendarWidget_selectionChanged();

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
