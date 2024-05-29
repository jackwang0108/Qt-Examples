#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->menubar->setNativeMenuBar(false);

    // 互斥中英文选项
    QActionGroup *actionGroup = new QActionGroup(this);
    actionGroup->addAction(ui->actLangEn);
    actionGroup->addAction(ui->actLangZh);
    actionGroup->setExclusive(true);

    // 添加无法通过UI编辑器可视化添加的组件

    // 字体大小
    QSpinBox *spinFontSize = new QSpinBox(this);
    spinFontSize->setMinimum(5);
    spinFontSize->setMaximum(50);
    spinFontSize->setValue(ui->textEdit->font().pointSize());
    spinFontSize->setMinimumWidth(50);
    ui->toolBar->addWidget(spinFontSize);

    // 字体
    QFontComboBox *comboFont = new QFontComboBox(this);
    comboFont->setMinimumWidth(150);
    comboFont->setFont(ui->textEdit->font());
    ui->toolBar->addWidget(comboFont);

    connect(spinFontSize, &QSpinBox::valueChanged, this, &MainWindow::do_fontSizeChanged);
    connect(comboFont, &QFontComboBox::currentFontChanged, this, &MainWindow::do_fontChanged);

    ui->toolBar->addSeparator();
    ui->toolBar->addAction(ui->actClose);

    // 状态栏
    labelFile = new QLabel(this);
    labelFile->setMinimumWidth(150);
    labelFile->setText("文件名: ");
    ui->statusbar->addWidget(labelFile);

    progressBar = new QProgressBar(this);
    progressBar->setMinimum(spinFontSize->maximum());
    progressBar->setMaximum(spinFontSize->maximum());
    progressBar->setValue(ui->textEdit->font().pointSize());
    ui->statusbar->addWidget(progressBar);

    labelInfo = new QLabel("Permanent");
    ui->statusbar->addPermanentWidget(labelInfo);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actFileNew_triggered()
{
    ui->textEdit->clear();
    ui->textEdit->document()->setModified(false);

    labelFile->setText("文件名: 新建文件");
}

void MainWindow::on_actFileOpen_triggered()
{
    labelFile->setText("正在打开文件");
}

void MainWindow::on_actFileSave_triggered()
{
    labelFile->setText("文件已保存");
    ui->textEdit->document()->setModified(true);
}

void MainWindow::on_textEdit_copyAvailable(bool b)
{
    ui->actEditCut->setEnabled(b);
    ui->actEditCopy->setEnabled(b);
    ui->actEditPaste->setEnabled(ui->textEdit->canPaste());
}

void MainWindow::on_textEdit_selectionChanged()
{
    QTextCharFormat currCharFmt = ui->textEdit->currentCharFormat();
    ui->actFontBold->setChecked(currCharFmt.font().bold());
    ui->actFontItalic->setChecked(currCharFmt.font().italic());
    ui->actFontUnderline->setChecked(currCharFmt.font().underline());
}

void MainWindow::on_actFontBold_triggered(bool checked)
{
    QTextCharFormat currCharFmt = ui->textEdit->currentCharFormat();

    if (checked)
        currCharFmt.setFontWeight(QFont::Bold);
    else
        currCharFmt.setFontWeight(QFont::Normal);

    ui->textEdit->setCurrentCharFormat(currCharFmt);
}

void MainWindow::on_actFontItalic_triggered(bool checked)
{
    QTextCharFormat currCharFmt = ui->textEdit->currentCharFormat();
    currCharFmt.setFontItalic(checked);
    ui->textEdit->setCurrentCharFormat(currCharFmt);
}

void MainWindow::on_actFontUnderline_triggered(bool checked)
{
    QTextCharFormat currCharFmt = ui->textEdit->currentCharFormat();
    currCharFmt.setFontUnderline(checked);
    ui->textEdit->setCurrentCharFormat(currCharFmt);
}

void MainWindow::do_fontSizeChanged(int fontSize)
{
    QTextCharFormat currCharFmt = ui->textEdit->currentCharFormat();
    currCharFmt.setFontPointSize(fontSize);
    ui->textEdit->setCurrentCharFormat(currCharFmt);
    progressBar->setValue(fontSize);
}

void MainWindow::do_fontChanged(const QFont &font)
{
    QTextCharFormat currCharFmt = ui->textEdit->currentCharFormat();
    currCharFmt.setFont(font);
    ui->textEdit->setCurrentCharFormat(currCharFmt);

    labelInfo->setText("字体名称: " + font.family());
}