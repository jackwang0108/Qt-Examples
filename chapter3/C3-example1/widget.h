#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

class TPerson;

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

private:
    TPerson *boy;
    TPerson *girl;

private slots:
    void do_ageChanged(quint8 newAge);
    void do_spinChanged(int arg1);
    void on_boyPushButton_clicked();
    void on_girlPushButton_clicked();
    void on_metaObjectInfoButton_clicked();
    void on_clearTextButton_clicked();

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
