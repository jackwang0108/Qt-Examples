#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QLabel>
#include <QMenuBar>
#include <QSpinBox>
#include <QMainWindow>
#include <QProgressBar>
#include <QActionGroup>
#include <QFontComboBox>

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
    QLabel *labelInfo;
    QLabel *labelFile;
    QProgressBar *progressBar;

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actFileNew_triggered();
    void on_actFileOpen_triggered();
    void on_actFileSave_triggered();

    void on_textEdit_selectionChanged();
    void on_textEdit_copyAvailable(bool b);

    void on_actFontBold_triggered(bool checked);
    void on_actFontItalic_triggered(bool checked);
    void on_actFontUnderline_triggered(bool checked);

    void do_fontSizeChanged(int fontSize);
    void do_fontChanged(const QFont &font);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
