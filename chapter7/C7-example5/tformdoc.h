#ifndef TFORMDOC_H
#define TFORMDOC_H

#include <QWidget>

namespace Ui
{
    class TFormDoc;
}

class TFormDoc : public QWidget
{
    Q_OBJECT

private:
    QString fileName;
    bool isOpened{false};

public:
    explicit TFormDoc(QWidget *parent = nullptr);
    ~TFormDoc();

    void loadFromFile(QString &filePath);
    QString currFileName();
    bool isFileOpened();
    bool saveToFile();

    void setEditorFont();
    void textCut();
    void textCopy();
    void textPaste();

private:
    Ui::TFormDoc *ui;
};

#endif // TFORMDOC_H
