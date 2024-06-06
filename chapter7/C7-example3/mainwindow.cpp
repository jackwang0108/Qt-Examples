#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include "tformdoc.h"
#include "TFormTable.h"

#include <QPixmap>
#include <QPainter>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    this->setCentralWidget(ui->tabWidget);

    ui->tabWidget->setVisible(false);
    ui->tabWidget->clear();
    ui->tabWidget->setTabsClosable(true);
    // setWindowState(Qt::WindowMaximized);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actWidgetInSide_triggered()
{
    TFormDoc *formDoc = new TFormDoc(this);
    formDoc->setAttribute(Qt::WA_DeleteOnClose);

    int curr = ui->tabWidget->addTab(formDoc, QString::asprintf("Doc %d", ui->tabWidget->count()));
    ui->tabWidget->setCurrentIndex(curr);
    ui->tabWidget->setVisible(true);

    connect(formDoc, &TFormDoc::titleChanged, this, &MainWindow::do_changeTableTitle);
}

void MainWindow::do_changeTableTitle(QString title)
{
    int index = ui->tabWidget->currentIndex();
    ui->tabWidget->setTabText(index, title);
}

void MainWindow::on_actWindowInSide_triggered()
{
    TFormTable *formTable = new TFormTable(this);
    formTable->setAttribute(Qt::WA_DeleteOnClose);

    int curr = ui->tabWidget->addTab(formTable, QString::asprintf("Doc %d", ui->tabWidget->count()));
    ui->tabWidget->setCurrentIndex(curr);
    ui->tabWidget->setVisible(true);
}

void MainWindow::on_actWindow_triggered()
{
    TFormTable *formTable = new TFormTable();
    formTable->setAttribute(Qt::WA_DeleteOnClose);
    formTable->setWindowTitle("基于QMainWindow的独立窗口");

    // formTable->setWindowOpacity(0.9);
    formTable->show();
}

void MainWindow::on_actWidget_triggered()
{
    TFormDoc *formDoc = new TFormDoc();
    formDoc->setAttribute(Qt::WA_DeleteOnClose);
    formDoc->setWindowTitle("基于QWidget的独立窗口");

    formDoc->setWindowOpacity(0.9);
    formDoc->show();
}

void MainWindow::on_tabWidget_tabCloseRequested(int index)
{
    ui->tabWidget->widget(index)->close();
}

void MainWindow::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    painter.drawPixmap(0, ui->toolBar->height(), width(), height() - ui->toolBar->height() - ui->statusBar->height(), QPixmap(":/images/images/back2.jpg"));
}
