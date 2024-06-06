#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QLabel>
#include <QMainWindow>
#include <QStandardItemModel>
#include <QItemSelectionModel>

#include "tdialogheaders.h"

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
    QLabel *labelCellPos;
    QLabel *labelCellText;

    QStandardItemModel *model;
    QItemSelectionModel *select;

    TDialogHeaders *dlgHeader;

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

signals:
    void cellIndexChanged(int row, int col);

private slots:
    void
    on_actTabSetSize_triggered();

    void on_actTabSetHeader_triggered();

    void on_actTabLocate_triggered();

    void do_setCellText(int row, int col, QString &text);

    void on_tableView_clicked(const QModelIndex &index);

    void on_model_currentChanged(const QModelIndex &index, const QModelIndex &prev);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
