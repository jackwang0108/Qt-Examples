#ifndef TDIALOGLOCATE_H
#define TDIALOGLOCATE_H

#include <QDialog>
#include <QShowEvent>
#include <QCloseEvent>

namespace Ui
{
    class TDialogLocate;
}

class TDialogLocate : public QDialog
{
    Q_OBJECT

public:
    void setSpinRange(int rowNum, int colNum);

public:
    explicit TDialogLocate(QWidget *parent = nullptr);
    ~TDialogLocate();

signals:
    void cellTextChanged(int row, int col, QString &text);

    void changeActionEnabled(bool enabled);

private slots:
    void
    on_btnOk_clicked();

public slots:
    void setSpinValue(int row, int col);

private:
    Ui::TDialogLocate *ui;

    // QWidget interface
protected:
    virtual void closeEvent(QCloseEvent *event) override;
    virtual void showEvent(QShowEvent *event) override;
};

#endif // TDIALOGLOCATE_H
