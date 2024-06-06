#include "tdialogheaders.h"
#include "ui_tdialogheaders.h"

TDialogHeaders::TDialogHeaders(QWidget *parent)
    : QDialog(parent), ui(new Ui::TDialogHeaders)
{
    ui->setupUi(this);

    model = new QStringListModel(this);
    ui->listView->setModel(model);
}

TDialogHeaders::~TDialogHeaders()
{
    delete ui;
}

void TDialogHeaders::setHeaderList(QStringList &list)
{
    model->setStringList(list);
}

QStringList TDialogHeaders::headerList()
{
    return model->stringList();
}