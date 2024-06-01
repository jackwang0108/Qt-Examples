#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include <QDir>
#include <QFileSystemModel>
#include <QRegularExpression>

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
    QFileSystemModel *model;

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actSetRootFolder_triggered();

    void on_radioFolderFile_clicked(bool checked);

    void on_radioFolderOnly_clicked(bool checked);

    void on_chkEnableFilter_clicked(bool checked);

    void on_comboFilter_currentIndexChanged(int index);

    void on_btnApplyFilter_clicked();

    void on_treeView_clicked(const QModelIndex &index);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
