#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include <QFileInfo>
#include <QSaveFile>
#include <QException>
#include <QTextBlock>
#include <QMessageBox>
#include <QFileDialog>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    this->setCentralWidget(ui->tabWidget);
}

MainWindow::~MainWindow()
{
    delete ui;
}

QString MainWindow::get_fileName(bool save)
{
    QString filter = "程序文件(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)";
    QString currPath = QCoreApplication::applicationDirPath();
    auto handler = save ? &QFileDialog::getSaveFileName : &QFileDialog::getOpenFileName;

    QString fileName = handler(this, "打开一个文件", currPath, filter, nullptr, QFileDialog::Options{});

    if (fileName.isEmpty())
        return fileName;

    QFileInfo fileInfo(fileName);
    QDir::setCurrent(fileInfo.absoluteFilePath());
    return fileName;
}

void MainWindow::on_actOpen_IODevice_triggered()
{
    QFile file(get_fileName(false));

    if (!file.exists())
        return;

    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    ui->textEditDevice->appendPlainText(file.readAll());

    file.close();
}

void MainWindow::on_actSave_IODevice_triggered()
{
    QString content = ui->textEditDevice->toPlainText();

    QFile file(get_fileName(true));
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
        return;

    file.write(content.toUtf8(), content.toUtf8().length());

    file.close();
}

void MainWindow::on_actSave_TextSafe_triggered()
{
    QString content = ui->textEditDevice->toPlainText();

    QSaveFile file(get_fileName(true));
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
        return;

    file.setDirectWriteFallback(false);
    try
    {
        file.write(content.toUtf8(), content.toUtf8().length());
        file.commit();
    }
    catch (QException &e)
    {
        QMessageBox::warning(this, "异常", "保存文件发生错误");
        file.cancelWriting();
    }
}

void MainWindow::on_actOpen_TextStream_triggered()
{
    QFile file(get_fileName(false));

    if (!file.exists())
        return;

    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    QTextStream stream(&file);
    stream.setAutoDetectUnicode(true);

    while (!stream.atEnd())
        ui->textEditStream->appendPlainText(stream.readLine());

    file.close();
}

void MainWindow::on_actSave_TextStream_triggered()
{
    QString content = ui->textEditDevice->toPlainText();

    QSaveFile file(get_fileName(true));
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
        return;

    file.setDirectWriteFallback(false);
    try
    {
        QTextStream stream(&file);
        stream.setAutoDetectUnicode(true);

        QTextDocument *doc = ui->textEditStream->document();

        for (int i = 0; i < doc->blockCount(); i++)
            stream << doc->findBlockByNumber(i).text() << "\n";

        file.commit();
    }
    catch (QException &e)
    {
        QMessageBox::warning(this, "异常", "保存文件发生错误");
        file.cancelWriting();
    }
}
