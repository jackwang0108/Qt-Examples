#include "tdicethread.h"

#include <QRandomGenerator>

TDiceThread::TDiceThread(QObject *parent)
    : QThread(parent)
{
}

void TDiceThread::run()
{
    isStop = false;
    isPause = true;

    while (!isStop)
    {
        if (!isPause)
        {
            seq++;
            diceValue = QRandomGenerator::global()->bounded(1, 7);
            emit newValue(seq, diceValue);
        }
        msleep(500);
    }

    quit();
}

void TDiceThread::diceBegin()
{
    isPause = false;
}

void TDiceThread::dicePause()
{
    isPause = true;
}

void TDiceThread::stopThread()
{
    isStop = true;
}
