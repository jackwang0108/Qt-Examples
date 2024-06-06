#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include "tformdoc.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    this->setCentralWidget(ui->mdiArea);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setActionStatus(QList<QAction *> actionList, bool enabled)
{
    for (auto action : actionList)
        action->setEnabled(enabled);
}

void MainWindow::on_actDoc_New_triggered()
{
    TFormDoc *formDoc = new TFormDoc(this);
    ui->mdiArea->addSubWindow(formDoc);
    formDoc->show();

    this->setActionStatus({ui->actCut, ui->actCopy, ui->actPaste, ui->actFont}, true);
}

void MainWindow::on_actDoc_Open_triggered()
{
    bool needNew = true;
    TFormDoc *formDoc;
    if (ui->mdiArea->subWindowList().size() > 0)
    {
        formDoc = dynamic_cast<TFormDoc *>(ui->mdiArea->activeSubWindow()->widget());
        needNew = formDoc->isFileOpened();
    }

    QString currPath = QCoreApplication::applicationDirPath();
    QString filePath = QFileDialog::getOpenFileName(this, "打开一个文件", currPath, "C++源文件(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)");

    if (filePath.isEmpty())
        return;

    if (needNew)
    {
        formDoc = new TFormDoc(this);
        ui->mdiArea->addSubWindow(formDoc);
    }

    formDoc->loadFromFile(filePath);
    formDoc->show();

    this->setActionStatus({ui->actCut, ui->actCopy, ui->actPaste, ui->actFont}, true);
}

void MainWindow::on_actDoc_Save_triggered()
{
    TFormDoc *formDoc = dynamic_cast<TFormDoc *>(ui->mdiArea->activeSubWindow()->widget());
    formDoc->saveToFile();
}

void MainWindow::on_actFont_triggered()
{
    TFormDoc *formDoc = dynamic_cast<TFormDoc *>(ui->mdiArea->activeSubWindow()->widget());
    formDoc->setEditorFont();
}

void MainWindow::on_actCut_triggered()
{
    TFormDoc *formDoc = dynamic_cast<TFormDoc *>(ui->mdiArea->activeSubWindow()->widget());
    formDoc->textCut();
}

void MainWindow::on_actCopy_triggered()
{
    TFormDoc *formDoc = dynamic_cast<TFormDoc *>(ui->mdiArea->activeSubWindow()->widget());
    formDoc->textCopy();
}

void MainWindow::on_actPaste_triggered()
{
    TFormDoc *formDoc = dynamic_cast<TFormDoc *>(ui->mdiArea->activeSubWindow()->widget());
    formDoc->textPaste();
}

void MainWindow::on_actViewMode_triggered(bool checked)
{
    if (checked)
        ui->mdiArea->setViewMode(QMdiArea::TabbedView);
    else
        ui->mdiArea->setViewMode(QMdiArea::SubWindowView);

    ui->mdiArea->setTabsClosable(checked);
    this->setActionStatus({ui->actCascade, ui->actTile}, !checked);
}

void MainWindow::on_actCascade_triggered()
{
    ui->mdiArea->cascadeSubWindows();
}

void MainWindow::on_actTile_triggered()
{
    ui->mdiArea->tileSubWindows();
}

void MainWindow::on_actCloseALL_triggered()
{
    ui->mdiArea->closeAllSubWindows();
}

void MainWindow::on_mdiArea_subWindowActivated(QMdiSubWindow *arg1)
{
    Q_UNUSED(arg1);

    bool enabled = true;
    if (ui->mdiArea->subWindowList().size() == 0)
        enabled = false;

    this->setActionStatus({ui->actCut, ui->actCopy, ui->actPaste, ui->actFont}, enabled);
}
