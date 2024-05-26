#include "mainwindow.h"

#include <QTimer>
#include <QPushButton>
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    // 使用metaObject获得当前对象的元对象
    QObject *btn = new QPushButton;
    // 元对象中保存了当前对象的类的类名, 属性等信息. 这里是获得类名, 即反射
    qDebug() << btn->metaObject()->className();

    // 可以使用qobject_cast来转换类型, 但是必须是子类和父类
    QPushButton *pushBtn = qobject_cast<QPushButton *>(btn);
    qDebug() << btn->metaObject()->className();

    // 元对象保存了类的子类和父类信息, 可以使用inherits来判断是否为某一个类的实例
    QTimer *timer = new QTimer();
    qDebug() << timer->inherits("QTimer");
    qDebug() << timer->inherits("QObject");
    qDebug() << timer->inherits("QPushButton");
    qDebug() << timer->inherits("QAbstractButton");

    // 也可以直接输出对象的名称
    qDebug() << timer->metaObject()->className();
    qDebug() << timer->metaObject()->superClass()->className();

    return 0;
}
