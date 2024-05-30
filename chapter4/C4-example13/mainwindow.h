#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QIcon>
#include <QLabel>
#include <QPixmap>
#include <QSpinBox>
#include <QMainWindow>
#include <QFileDialog>
#include <QTreeWidgetItem>

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
    enum treeColumn
    {
        colItem = 0,
        colItemType = 1,
        colDate = 2
    };

    enum treeItemType
    {
        itTopItem = 1001,
        itGroupItem = 1002,
        itImageItem = 10003,
    };

    QLabel *labelFileName;
    QLabel *labelNodeText;

    // 放大倍数
    QSpinBox *scaleRatio;
    QPixmap pixMap;

    float ratio;

private:
    void displayImage(QTreeWidgetItem *curr);
    void setupTreeWidgetHeader(QStringList strList);
    void recursiveChangeCaption(QTreeWidgetItem *curr);

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actAddDir_triggered();
    void on_actAddFile_triggered();
    void on_actDeleteItem_triggered();
    void on_actScanItems_triggered();

    void on_actZoomIn_triggered();
    void on_actZoomOut_triggered();
    void on_actZoomFitWidth_triggered();
    void on_actZoomFitHeight_triggered();
    void on_actRealSize_triggered();

    void on_actDockVisible_triggered(bool checked);
    void on_actDockFloat_triggered(bool checked);

    void on_treeWidget_currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous);

    void on_dockWidget_visibilityChanged(bool visible);
    void on_dockWidget_topLevelChanged(bool topLevel);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
