#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui {

// 自动生成的ui_widget.h中定义的类，这里提供一个外部声明
class Widget;
}
QT_END_NAMESPACE

class Widget : public QWidget
{
    // QT的宏， 使用QT信号与槽机制必须添加
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    Ui::Widget *ui; // 指向可视化界面本身的指针
};
#endif // WIDGET_H
