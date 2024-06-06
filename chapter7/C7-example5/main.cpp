#include "mainwindow.h"
#include "tlogindialog.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    TLoginDialog *login = new TLoginDialog;

    if (login->exec() == QDialog::Accepted)
    {
        MainWindow w;
        w.show();
        return a.exec();
    }
    else
        return 1;
}
