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

private slots:
    void do_doubleClick();

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    Ui::Widget *ui;

    // QWidget interface
protected:
    virtual void mouseDoubleClickEvent(QMouseEvent *event) override;
};
#endif // WIDGET_H
