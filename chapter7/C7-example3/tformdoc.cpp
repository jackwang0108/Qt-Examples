#include "tformdoc.h"
#include "ui_tformdoc.h"

#include <QFont>
#include <QFile>
#include <QList>
#include <QAction>
#include <QToolBar>
#include <QFileInfo>
#include <QFontDialog>
#include <QFileDialog>
#include <QVBoxLayout>

TFormDoc::TFormDoc(QWidget *parent)
    : QWidget(parent), ui(new Ui::TFormDoc)
{
    ui->setupUi(this);

    QToolBar *locToolBar = new QToolBar("文档", this);

    QList<QAction *> actions{
        ui->actOpen,
        ui->actFont,
        locToolBar->addSeparator(),
        ui->actCut,
        ui->actCopy,
        ui->actPaste,
        ui->actRedo,
        ui->actUndo,
        locToolBar->addSeparator(),
        ui->actClose};
    locToolBar->addActions(actions);

    locToolBar->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);

    QVBoxLayout *layout = new QVBoxLayout();
    layout->addWidget(locToolBar);
    layout->addWidget(ui->plainTextEdit);
    this->setLayout(layout);
}

TFormDoc::~TFormDoc()
{
    delete ui;
}

void TFormDoc::on_actFont_triggered()
{
    QFont font = ui->plainTextEdit->font();

    bool ok;
    font = QFontDialog::getFont(&ok, font, this);

    if (!ok)
        return;

    ui->plainTextEdit->setFont(font);
}

void TFormDoc::on_actOpen_triggered()
{
    QString currPath = QCoreApplication::applicationDirPath();

    QString filePath = QFileDialog::getOpenFileName(this, "选择打开的文件", currPath, "C++程序文件(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)");
    if (filePath.isEmpty())
        return;

    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    ui->plainTextEdit->clear();

    QTextStream stream(&file);
    while (!stream.atEnd())
    {
        QString str = stream.readLine();
        ui->plainTextEdit->appendPlainText(str);
    }

    file.close();

    QFileInfo info(filePath);
    QString fileName = info.fileName();
    this->setWindowTitle(fileName);

    emit titleChanged(fileName);
}
