#include "tmylabel.h"

TMyLabel::TMyLabel(QWidget *parent) : QLabel{parent}
{
    setAttribute(Qt::WA_Hover, true);
}

void TMyLabel::mouseDoubleClickEvent(QMouseEvent *event)
{
    Q_UNUSED(event);
    emit doubleClicked();
}

bool TMyLabel::event(QEvent *event)
{
    if (event->type() == QEvent::HoverEnter)
    {
        QPalette palette = this->palette();
        palette.setColor(QPalette::WindowText, Qt::red);
        this->setPalette(palette);
    }
    else if (event->type() == QEvent::HoverLeave)
    {
        QPalette palette = this->palette();
        palette.setColor(QPalette::WindowText, Qt::black);
        this->setPalette(palette);
    }

    return QLabel::event(event);
}
