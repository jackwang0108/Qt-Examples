#ifndef TPERSON_H
#define TPERSON_H

#include <QObject>

class TPerson : public QObject
{
    Q_OBJECT

    Q_CLASSINFO("author", "Jack Wang");
    Q_CLASSINFO("compony", "Test");
    Q_CLASSINFO("version", "1.0.0");

    Q_PROPERTY(QString name MEMBER m_name)
    Q_PROPERTY(int score MEMBER m_score)
    Q_PROPERTY(int age READ age WRITE setAge NOTIFY ageChanged)
public:
    explicit TPerson(QString name, QObject *parent = nullptr);
    ~TPerson();

    int age();
    void setAge(quint8 age);
    int incAge();

signals:
    void ageChanged(quint8 newAge);

private:
    QString m_sex;
    QString m_name;
    quint8 m_age = 10;
    quint8 m_score = 80;
};

#endif // TPERSON_H
