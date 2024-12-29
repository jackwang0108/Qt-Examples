#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include <QFileDialog>

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

private:
    QString get_fileName(bool save = false);

private slots:

    void on_actOpen_IODevice_triggered();

    void on_actSave_IODevice_triggered();

    void on_actSave_TextSafe_triggered();

    void on_actOpen_TextStream_triggered();

    void on_actSave_TextStream_triggered();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
