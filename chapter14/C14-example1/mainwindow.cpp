#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include <QPixmap>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    threadA = new TDiceThread(this);
    connect(threadA, &TDiceThread::started, this, &MainWindow::do_threadA_started);
    connect(threadA, &TDiceThread::finished, this, &MainWindow::do_threadA_finished);
    connect(threadA, &TDiceThread::newValue, this, &MainWindow::do_threadA_newValue);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::do_threadA_started()
{
    ui->statusbar->showMessage("Thread状态: Thread Started");

    ui->actThread_Run->setEnabled(false);
    ui->actThread_Quit->setEnabled(true);

    ui->actDice_Run->setEnabled(true);
    ui->actDice_Pause->setEnabled(false);
}

void MainWindow::do_threadA_finished()
{
    ui->statusbar->showMessage("Thread状态: Thread Finished");

    ui->actThread_Run->setEnabled(true);
    ui->actThread_Quit->setEnabled(false);

    ui->actDice_Run->setEnabled(false);
    ui->actDice_Pause->setEnabled(false);
}

void MainWindow::do_threadA_newValue(int seq, int diceValue)
{
    QString str = QString::asprintf("第%d次掷骰子, 点数: %d", seq, diceValue);
    ui->plainTextEdit->appendPlainText(str);

    QString filename = QString::asprintf(":/dice/images/d%d.jpg", diceValue);
    QPixmap pixmap(filename);
    ui->labPic->setPixmap(pixmap);
}

void MainWindow::on_actThread_Run_triggered()
{
    threadA->start();
}

void MainWindow::on_actDice_Run_triggered()
{
    threadA->diceBegin();
    ui->actDice_Run->setEnabled(false);
    ui->actDice_Pause->setEnabled(true);
}

void MainWindow::on_actDice_Pause_triggered()
{
    threadA->dicePause();

    ui->actDice_Run->setEnabled(true);
    ui->actDice_Pause->setEnabled(false);
}

void MainWindow::on_actThread_Quit_triggered()
{
    threadA->stopThread();

    QString filename = QString(":/dice/images/d0.jpg");
    QPixmap pixmap(filename);
    ui->labPic->setPixmap(pixmap);
}

void MainWindow::on_actClear_triggered()
{
    ui->plainTextEdit->clear();
}

void MainWindow::closeEvent(QCloseEvent *event)
{
    if (threadA->isRunning())
    {
        threadA->terminate();
        threadA->wait();
    }
    event->accept();
}
