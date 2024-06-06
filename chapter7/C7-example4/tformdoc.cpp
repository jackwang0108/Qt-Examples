#include "tformdoc.h"
#include "ui_tformdoc.h"

#include <QFile>
#include <QFont>
#include <QFileInfo>
#include <QFontDialog>
#include <QTextStream>

TFormDoc::TFormDoc(QWidget *parent)
    : QWidget(parent), ui(new Ui::TFormDoc)
{
    ui->setupUi(this);

    setWindowTitle("New Doc[*]");
    setAttribute(Qt::WA_DeleteOnClose);
    connect(ui->plainTextEdit, &QPlainTextEdit::modificationChanged, this, &TFormDoc::setWindowModified);
}

TFormDoc::~TFormDoc()
{
    delete ui;
}

void TFormDoc::loadFromFile(QString &filePath)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    QTextStream stream(&file);
    ui->plainTextEdit->clear();
    ui->plainTextEdit->setPlainText(stream.readAll());

    file.close();

    QFileInfo info(filePath);
    this->setWindowTitle(info.fileName() + "[*]");

    fileName = info.fileName();
    isOpened = true;
}

QString TFormDoc::currFileName()
{
    return fileName;
}

bool TFormDoc::isFileOpened()
{
    return isOpened;
}

bool TFormDoc::saveToFile()
{
    this->setWindowModified(false);
    return true;
}

void TFormDoc::setEditorFont()
{
    QFont font = ui->plainTextEdit->font();

    bool ok = false;
    font = QFontDialog::getFont(&ok, font);
    if (ok)
        ui->plainTextEdit->setFont(font);
}

void TFormDoc::textCut()
{
    ui->plainTextEdit->cut();
}

void TFormDoc::textCopy()
{
    ui->plainTextEdit->copy();
}

void TFormDoc::textPaste()
{
    ui->plainTextEdit->paste();
}
