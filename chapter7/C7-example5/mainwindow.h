#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QList>
#include <QAction>
#include <QMainWindow>
#include <QFileDialog>
#include <QMdiSubWindow>

QT_BEGIN_NAMESPACE
namespace Ui
{
    class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

private:
    void setActionStatus(QList<QAction *> actionList, bool enabled);

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actDoc_New_triggered();

    void on_actDoc_Open_triggered();

    void on_actDoc_Save_triggered();

    void on_actFont_triggered();

    void on_actCut_triggered();

    void on_actCopy_triggered();

    void on_actPaste_triggered();

    void on_actViewMode_triggered(bool checked);

    void on_actCascade_triggered();

    void on_actTile_triggered();

    void on_actCloseALL_triggered();

    void on_mdiArea_subWindowActivated(QMdiSubWindow *arg1);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
