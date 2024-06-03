#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

#include <QUrl>
#include <QSize>
#include <QPixmap>
#include <QFileInfo>
#include <QMimeData>
#include <QDropEvent>
#include <QResizeEvent>
#include <QDragEnterEvent>

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
    Ui::Widget *ui;

    // QWidget interface
protected:
    virtual void resizeEvent(QResizeEvent *event) override;
    virtual void dragEnterEvent(QDragEnterEvent *event) override;
    virtual void dropEvent(QDropEvent *event) override;
};
#endif // WIDGET_H
