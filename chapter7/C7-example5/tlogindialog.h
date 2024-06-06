#ifndef TLOGINDIALOG_H
#define TLOGINDIALOG_H

#include <QPoint>
#include <QDialog>

namespace Ui
{
    class TLoginDialog;
}

class TLoginDialog : public QDialog
{
    Q_OBJECT

private:
    bool moving{false};
    QPoint lastPosition;

    QString user{"user"};
    QString pass{"12345"};
    int currTryTimes{0};
    const int maxTryTimes{3};

    QString encrypt(const QString &str);

    void readSettings();
    void writeSettings();

public:
    explicit TLoginDialog(QWidget *parent = nullptr);
    ~TLoginDialog();

private:
    Ui::TLoginDialog *ui;

    // QWidget interface
protected:
    virtual void mousePressEvent(QMouseEvent *event) override;
    virtual void mouseReleaseEvent(QMouseEvent *event) override;
    virtual void mouseMoveEvent(QMouseEvent *event) override;
private slots:
    void on_btnOk_clicked();
};

#endif // TLOGINDIALOG_H
