#ifndef TDICETHREAD_H
#define TDICETHREAD_H

#include <QThread>

class TDiceThread : public QThread
{
    Q_OBJECT
public:
    TDiceThread(QObject *parent = nullptr);

private:
    int seq = 0;
    int diceValue = -1;
    bool isPause = false;
    bool isStop = false;

public:
    void diceBegin();
    void dicePause();
    void stopThread();

protected:
    void run() override;

signals:
    void newValue(int seq, int diceValue);
};

#endif // TDICETHREAD_H
