#include "widget.h"
#include "./ui_widget.h"
#include "tperson.h"

#include <QMetaObject>
#include <QMetaProperty>
#include <QMetaClassInfo>

Widget::Widget(QWidget *parent)
    : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    boy = new TPerson("小明", this);
    girl = new TPerson("小红", this);

    // 初始化年龄
    boy->setAge(ui->boySpinBox->value());
    girl->setAge(ui->girlSpinBox->value());

    // 设置TPerson类的元对象属性
    boy->setProperty("sex", "boy");
    girl->setProperty("sex", "girl");

    // 连接自定义的信号到槽
    connect(boy, SIGNAL(ageChanged(quint8)), this, SLOT(do_ageChanged(quint8)));
    connect(girl, SIGNAL(ageChanged(quint8)), this, SLOT(do_ageChanged(quint8)));

    // 设置SpinBox类的元对象属性
    ui->boySpinBox->setProperty("isBoy", true);
    ui->girlSpinBox->setProperty("isBoy", false);

    // 连接SpinBox的信号到槽
    connect(ui->boySpinBox, SIGNAL(valueChanged(int)), this, SLOT(do_spinChanged(int)));
    connect(ui->girlSpinBox, SIGNAL(valueChanged(int)), this, SLOT(do_spinChanged(int)));
}

Widget::~Widget()
{
    delete ui;
}

void Widget::do_ageChanged(quint8 newAge)
{
    TPerson *person = qobject_cast<TPerson *>(sender());

    QString str = QString("%1, 性别=%2, 年龄=%3")
                      .arg(person->property("name").toString())
                      .arg(person->property("sex").toString())
                      .arg(newAge);
    ui->plainTextEdit->appendPlainText(str);
}

void Widget::do_spinChanged(int arg1)
{
    QSpinBox *spinBox = qobject_cast<QSpinBox *>(sender());

    if (spinBox->property("isBoy").toBool())
        boy->setAge(arg1);
    else
        girl->setAge(arg1);
}

void Widget::on_boyPushButton_clicked()
{
    boy->incAge();
    ui->boySpinBox->setValue(boy->age());
}

void Widget::on_girlPushButton_clicked()
{
    girl->incAge();
    ui->girlSpinBox->setValue(girl->age());
}

void Widget::on_metaObjectInfoButton_clicked()
{
    const QMetaObject *meta = boy->metaObject();

    QString str = QString("类名称: %1\n").arg(meta->className());
    ui->plainTextEdit->appendPlainText(str);

    for (int i = meta->propertyOffset(); i < meta->propertyCount(); i++)
    {
        const char *pName = meta->property(i).name();
        QString pValue = boy->property(pName).toString();

        QString str = QString("属性名称=%1, 属性值=%2\n")
                          .arg(pName)
                          .arg(pValue);
        ui->plainTextEdit->appendPlainText(str);
    }

    ui->plainTextEdit->appendPlainText("类信息 (ClassInfo):");
    for (int i = meta->classInfoOffset(); i < meta->classInfoCount(); i++)
    {
        QMetaClassInfo cInfo = meta->classInfo(i);

        QString str = QString("name=%1, value=%2")
                          .arg(cInfo.name())
                          .arg(cInfo.value());

        ui->plainTextEdit->appendPlainText(str);
    }
}

void Widget::on_clearTextButton_clicked()
{
    ui->plainTextEdit->clear();
}
