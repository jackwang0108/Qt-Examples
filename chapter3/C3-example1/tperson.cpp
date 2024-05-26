#include "tperson.h"

TPerson::TPerson(QString name, QObject *parent)
    : QObject{parent}, m_name{name}
{
}

TPerson::~TPerson()
{
    qDebug("TPerson对象被删除");
}

int TPerson::age()
{
    return m_age;
}

void TPerson::setAge(quint8 age)
{
    if (age == m_age)
        return;

    m_age = age;
    emit ageChanged(m_age);
}

int TPerson::incAge()
{
    m_age += 1;
    emit ageChanged(m_age);
    return m_age;
}
