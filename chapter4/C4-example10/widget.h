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
    void on_btnClear_clicked();

    void on_btnInitItems_clicked();
    void on_chkEditable_clicked(bool);
    void on_btnClearItems_clicked();
    void on_comboItems_currentTextChanged(const QString &);

    void on_btnInitCities_clicked();
    void on_comboCities_currentIndexChanged(int);

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
