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
    void on_btnAlignLeft_clicked();
    void on_btnAlignCenter_clicked();
    void on_btnAlignRight_clicked();

    void on_btnFontBold_clicked(bool checked);
    void on_btnFontItalic_clicked(bool checked);
    void on_btnFontUnderline_clicked(bool checked);

    void on_checkReadOnly_clicked(bool checked);
    void on_checkEnabled_clicked(bool checked);
    void on_checkClearEnabled_clicked(bool checked);

    void on_radioBlack_clicked();
    void on_radioRed_clicked();
    void on_radioBlue_clicked();

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
