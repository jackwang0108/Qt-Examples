#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui
{
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actWidgetInSide_triggered();

    void on_actWindowInSide_triggered();

    void on_actWindow_triggered();

    void on_actWidget_triggered();

    void do_changeTableTitle(QString title);

    void on_tabWidget_tabCloseRequested(int index);

private:
    Ui::MainWindow *ui;

    // QWidget interface
protected:
    virtual void paintEvent(QPaintEvent *event) override;
};
#endif // MAINWINDOW_H
