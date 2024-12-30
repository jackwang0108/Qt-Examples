#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include <QFloat16>
#include <QMessageBox>
#include <QFileDialog>
#include <QFontDialog>
#include <QColorDialog>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->groupBox->setEnabled(false);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnFile_clicked()
{
    filename = QFileDialog::getSaveFileName(this, "选择一个文件", QApplication::applicationDirPath(), "数据流文件(*.stream)");

    if (filename.isEmpty())
        return;

    ui->editFilename->setText(filename);

    ui->actReadALL->setEnabled(true);
    ui->actSaveALL->setEnabled(false);

    ui->groupBox->setEnabled(true);
}

void MainWindow::on_btnFont_In_clicked()
{

    bool ok = false;
    QFont font = ui->btnFont_In->font();

    font = QFontDialog::getFont(&ok, this);
    if (ok)
        ui->btnFont_In->setFont(font);
}

void MainWindow::on_btnColor_In_clicked()
{
    QPalette palette = ui->btnColor_In->palette();

    QColor color = palette.buttonText().color();
    color = QColorDialog::getColor(color, this);
    if (!color.isValid())
        return;

    palette.setColor(QPalette::ButtonText, color);
    ui->btnColor_In->setPalette(palette);
}

void MainWindow::on_btnInt8_Write_clicked()
{
    qint8 value = ui->spin_Int8->value();
    writeByStream(value);
}

void MainWindow::on_btnInt8_Read_clicked()
{
    qint8 value;
    readByStream(value);
    ui->edit_Int8->setText(QString("%1").arg(value));
}

void MainWindow::on_btnUInt8_Write_clicked()
{
    quint8 value = ui->spin_UInt8->value();
    writeByStream(value);
}

void MainWindow::on_btnUInt8_Read_clicked()
{
    quint8 value;
    readByStream(value);
    ui->edit_UInt8->setText(QString("%1").arg(value));
}

void MainWindow::on_btnInt16_Write_clicked()
{
    qint16 value = ui->spin_Int16->value();
    writeByStream(value);
}

void MainWindow::on_btnInt16_Read_clicked()
{
    qint16 value;
    readByStream(value);
    ui->edit_Int16->setText(QString("%1").arg(value));
}

void MainWindow::on_btnUInt16_Write_clicked()
{
    quint16 value = ui->spin_UInt16->value();
    writeByStream(value);
}

void MainWindow::on_btnUIn16_Read_clicked()
{
    quint16 value;
    readByStream(value);
    ui->edit_Int16->setText(QString("%1").arg(value));
}

void MainWindow::on_btnInt32_Write_clicked()
{
    quint32 value = ui->spin_Int32->value();
    writeByStream(value);
}

void MainWindow::on_btnInt32_Read_clicked()
{
    qint32 value;
    readByStream(value);
    ui->edit_Int32->setText(QString("%1").arg(value));
}

void MainWindow::on_btnInt64_Write_clicked()
{
    qint64 value = ui->spin_Int64->value();
    writeByStream(value);
}

void MainWindow::on_btnInt64_Read_clicked()
{
    qint64 value;
    readByStream(value);
    ui->edit_Int64->setText(QString("%1").arg(value));
}

void MainWindow::on_btnBool_Write_clicked()
{
    bool value = ui->chkBox_In->isChecked();
    writeByStream(value);
}

void MainWindow::on_btnBool_Read_clicked()
{
    bool value;
    readByStream(value);
    ui->chkBox_Out->setChecked(value);
}

void MainWindow::on_btnInt_Write_clicked()
{
    qfloat16 value = ui->spin_Float16->value();
    writeByStream(value);
}

void MainWindow::on_btnInt_Read_clicked()
{
    qfloat16 value;
    readByStream(value);
    ui->edit_Float16->setText(QString::asprintf("%.02f", static_cast<float>(value)));
}

void MainWindow::on_btnFloat_Write_clicked()
{
    float value = ui->spin_Float->value();
    writeByStream(value);
}

void MainWindow::on_btnFloat_Read_clicked()
{
    float value;
    readByStream(value);
    ui->edit_Float->setText(QString::asprintf("%.02f", static_cast<float>(value)));
}

void MainWindow::on_btnDouble_Write_clicked()
{
    double value = ui->spin_Double->value();
    writeByStream(value);
}

void MainWindow::on_btnDouble_Read_clicked()
{
    double value;
    readByStream(value);
    ui->edit_Double->setText(QString::asprintf("%.04f", value));
}

void MainWindow::on_btnStr_Write_clicked()
{
    QString str = ui->editStr_In->text();
    char *c_str = str.toLocal8Bit().data();
    writeByStream(c_str);
}

void MainWindow::on_btnStr_Read_clicked()
{
    char *c_str;
    readByStream(c_str);
    QString str(c_str);
    ui->editStr_Out->setText(str);
}

void MainWindow::on_btnQStr_Write_clicked()
{
    QString str = ui->editQStr_In->text();
    writeByStream(str);
}

void MainWindow::on_btnQStr_Read_clicked()
{
    QString value;
    readByStream(value);
    ui->editQStr_Out->setText(value);
}

void MainWindow::on_btnFont_Write_clicked()
{
    QFont font = ui->btnFont_In->font();
    writeByStream(font);
}

void MainWindow::on_btnFont_Read_clicked()
{
    QFont font;
    readByStream(font);
    ui->editFont_Out->setFont(font);
}

void MainWindow::on_btnColor_Write_clicked()
{
    QPalette palette = ui->btnColor_In->palette();
    QColor color = palette.buttonText().color();
    writeByStream(color);
}

void MainWindow::on_btnColor_Read_clicked()
{
    QColor color;
    readByStream(color);
    QPalette palette = ui->editColor_Out->palette();
    palette.setColor(QPalette::Text, color);
    ui->editColor_Out->setPalette(palette);
}

void MainWindow::on_actSaveALL_triggered()
{
    QFile file(filename);
    if (!file.open(QIODevice::WriteOnly))
        return;

    QDataStream fileStream(&file);
    fileStream.setVersion(QDataStream::Qt_6_6);

    QDataStream::ByteOrder byteOrder = ui->radio_BigEndian->isChecked() ? QDataStream::BigEndian : QDataStream::LittleEndian;
    fileStream.setByteOrder(byteOrder);

    QDataStream::FloatingPointPrecision precision = ui->radio_Single->isChecked() ? QDataStream::SinglePrecision : QDataStream::DoublePrecision;
    fileStream.setFloatingPointPrecision(precision);

    fileStream << ui->spin_Int8->value()
               << ui->spin_UInt8->value()
               << ui->spin_Int16->value()
               << ui->spin_Int32->value()
               << ui->spin_Int64->value()
               << ui->btnBool_Read->isChecked()
               << ui->spin_Float16->value()
               << ui->spin_Float->value()
               << ui->spin_Double->value();

    QString str = ui->editStr_In->text();
    fileStream << str.toLocal8Bit().data();

    fileStream << ui->editQStr_In->text()
               << ui->btnFont_In->font()
               << ui->btnColor_In->palette().buttonText().color();

    file.close();
}

void MainWindow::on_actReadALL_triggered()
{
    if (!QFile::exists(filename))
        return;

    QFile fileDevice(filename);
    if (!fileDevice.open(QIODevice::ReadOnly))
        return;

    QDataStream fileStream(&fileDevice);
    fileStream.setVersion(QDataStream::Qt_6_2);
    if (ui->radio_BigEndian->isChecked())
        fileStream.setByteOrder(QDataStream::BigEndian);
    else
        fileStream.setByteOrder(QDataStream::LittleEndian);

    if (ui->radio_Single->isChecked())
        fileStream.setFloatingPointPrecision(QDataStream::SinglePrecision);
    else
        fileStream.setFloatingPointPrecision(QDataStream::DoublePrecision);

    fileStream.startTransaction();

    qint8 int8_Value = 0;
    fileStream >> int8_Value; // qint8
    ui->edit_Int8->setText(QString("%1").arg(int8_Value));

    quint8 uint8_Value = 0;
    fileStream >> uint8_Value; // quint8
    ui->edit_UInt8->setText(QString("%1").arg(uint8_Value));

    qint16 int16_Value = 0;
    fileStream >> int16_Value; // qint16
    ui->edit_Int16->setText(QString("%1").arg(int16_Value));

    quint16 uint16_Value;
    fileStream >> uint16_Value; // quint16
    ui->edit_UInt16->setText(QString("%1").arg(uint16_Value));

    qint32 int32_Value = 0;
    fileStream >> int32_Value; // qint32
    ui->edit_Int32->setText(QString("%1").arg(int32_Value));

    qint64 int64_Value = 0;
    fileStream >> int64_Value; // qint64
    ui->edit_Int64->setText(QString("%1").arg(int64_Value));

    bool bool_Value;
    fileStream >> bool_Value; // bool
    ui->chkBox_Out->setChecked(bool_Value);

    qfloat16 float16_Value = 0;
    fileStream >> float16_Value; // qfloat16
    float val = float16_Value;
    ui->edit_Float16->setText(QString::asprintf("%.2f", val));

    float float_Value = 0;
    fileStream >> float_Value; // float
    ui->edit_Float->setText(QString::asprintf("%.4f", float_Value));

    double double_Value = 0;
    fileStream >> double_Value; // double
    ui->edit_Double->setText(QString::asprintf("%.4f", double_Value));

    char *charStr;
    fileStream >> charStr; // char* 字符串
    QString str(charStr);  // 转换为QString字符串
    ui->editStr_Out->setText(str);

    QString str_Value = "";
    fileStream >> str_Value; // QString
    ui->editQStr_Out->setText(str_Value);

    QFont font;
    fileStream >> font; // QFont
    ui->editFont_Out->setFont(font);

    QColor color;
    fileStream >> color; // QColor
    QPalette palette = ui->editColor_Out->palette();
    palette.setColor(QPalette::Text, color);
    ui->editColor_Out->setPalette(palette);

    if (fileStream.commitTransaction())
        QMessageBox::information(this, "消息", "读取成功！");
    else
        QMessageBox::critical(this, "消息", "读取过程中有错误！");
    fileDevice.close();
}
