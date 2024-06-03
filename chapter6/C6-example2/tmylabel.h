#ifndef TMYLABEL_H
#define TMYLABEL_H

#include <QEvent>
#include <QLabel>
#include <QObject>

class TMyLabel : public QLabel
{
    Q_OBJECT

signals:
    void doubleClicked();

public:
    TMyLabel(QWidget *parent = nullptr);

    // QWidget interface
protected:
    virtual void mouseDoubleClickEvent(QMouseEvent *event) override;

    // QObject interface
public:
    virtual bool event(QEvent *event) override;
};

#endif // TMYLABEL_H
