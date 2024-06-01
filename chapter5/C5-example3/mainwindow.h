#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QFile>
#include <QLabel>
#include <QMainWindow>
#include <QModelIndex>
#include <QFileDialog>
#include <QRegularExpression>
#include <QStandardItemModel>
#include <QItemSelectionModel>

#include "tcomboboxdelegate.h"
#include "tspinboxdelegate.h"
#include "tfloatspinboxdelegate.h"

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
    QLabel *labelCurrFile;
    QLabel *labelCellPos;
    QLabel *labelCellText;
    const int fixedColumnCount = 6;

    QStandardItemModel *standardModel;
    QItemSelectionModel *selectionModel;

    TSpinboxDelegate *intSpinboxDelegate;
    TFloatSpinboxDelegate *floatSpinboxDelegate;
    TComboBoxDelegate *comboBoxDelegate;

private:
    void do_currentSelectionChanged(const QModelIndex &curr, const QModelIndex &prev);

    void initModelData(const QStringList &fileContent);

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actOpen_triggered();

    void on_actSave_triggered();

    void on_actAppend_triggered();

    void on_actInsert_triggered();

    void on_actDelete_triggered();

    void on_actModelData_triggered();

    void on_actAlignLeft_triggered();

    void on_actAlignCenter_triggered();

    void on_actAlignRight_triggered();

    void on_actFontBold_triggered(bool checked);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
