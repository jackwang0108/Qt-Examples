#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QFont>
#include <QDate>
#include <QIcon>
#include <QLabel>
#include <QMainWindow>
#include <QRandomGenerator>
#include <QTableWidgetItem>

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
    enum ColumnFieldNum
    {
        colName = 0,
        colSex,
        colBirth,
        colNationality,
        colParty,
        colScore,
    };

    enum CellType
    {
        ctName = 1000,
        ctSex,
        ctBirth,
        ctNationality,
        ctParty,
        ctScore
    };

    QLabel *labelCellIndex;
    QLabel *labelCellType;
    QLabel *labelStuID;

private:
    void createTableRow(int rowIdx, QString name, QString sex, QDate birthday, QString nationality, bool isParty, int score);

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_btnSetHHeader_clicked();
    void on_btnSetColumns_clicked();

    void on_btnTableInit_clicked();
    void on_btnTableInsert_clicked();
    void on_btnTableAppend_clicked();
    void on_btnTableDelete_clicked();

    void on_btnAutoHeight_clicked();
    void on_btnAutoWidth_clicked();

    void on_btnReadtoEdit_clicked();

    void on_chkColorRow_clicked(bool checked);

    void on_chkTableEditable_clicked(bool checked);

    void on_btnShowHHeader_clicked(bool checked);

    void on_btnShowVHeader_clicked(bool checked);

    void on_radioRowSelect_clicked();

    void on_radioCellSelect_clicked();

    void on_tableWidget_currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
