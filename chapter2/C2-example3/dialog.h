#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>
#include <QCheckBox>
#include <QPushButton>
#include <QRadioButton>
#include <QPlainTextEdit>

class Dialog : public QDialog
{
    Q_OBJECT

private:
    // checkbox
    QCheckBox *chkBoxBold;
    QCheckBox *chkBoxUnder;
    QCheckBox *chkBoxItalic;

    // radio button
    QRadioButton *radioRed;
    QRadioButton *radioBlue;
    QRadioButton *radioBlack;

    // plain input
    QPlainTextEdit *txtEdit;

    // buttons
    QPushButton *btnOk;
    QPushButton *btnClose;
    QPushButton *btnCancel;

private slots:
    void do_chkBoxUnder(bool checked);
    void do_chkBoxBold(bool checked);
    void do_chkBoxItalic(bool checked);

    void do_setFontColor();

    void do_clearTxtEdit();

public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();
};
#endif // DIALOG_H
