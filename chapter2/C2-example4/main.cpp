#include <QCoreApplication>

int main(int argc, char *argv[])
{
    qDebug() << QT_VERSION_STR;

    QString str;
    qDebug() << str.asprintf("0X%0X", QT_VERSION);

    return 0;
}
