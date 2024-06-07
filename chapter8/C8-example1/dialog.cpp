#include "dialog.h"
#include "./ui_dialog.h"

#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QFileDialog>
#include <QTemporaryDir>
#include <QTemporaryFile>

QString Dialog::getButtonStr(QPushButton *button)
{
    return button->text() + ", " + button->toolTip() + ":\n";
}

void Dialog::do_directoryChanged(const QString &path)
{
    ui->plainTextEdit->appendPlainText(path + "目录发生了改变");
}

void Dialog::do_fileChanged(const QString &path)
{
    ui->plainTextEdit->appendPlainText(path + "文件发生了改变");
}

Dialog::Dialog(QWidget *parent)
    : QDialog(parent), ui(new Ui::Dialog)
{
    ui->setupUi(this);

    watcher = new QFileSystemWatcher(this);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_pushButton_41_clicked()
{
    QString currDir = QCoreApplication::applicationDirPath();
    QString filePath = QFileDialog::getOpenFileName(this, "打开一个文件", currDir, "所有文件(*.*)");

    ui->editFile->setText(filePath);
}

void Dialog::on_pushButton_45_clicked()
{
    QString currDir = QCoreApplication::applicationDirPath();
    QString dirPath = QFileDialog::getExistingDirectory(this, "打开一个目录", currDir);

    ui->editDir->setText(dirPath);
}

void Dialog::on_pushButton_5_clicked()
{
    ui->editFile->clear();
    ui->editDir->clear();
}

void Dialog::on_pushButton_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);

    QString currDir = QCoreApplication::applicationDirPath();
    ui->plainTextEdit->appendPlainText(buttonStr + currDir);
}

void Dialog::on_pushButton_2_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);

    QString appFilePath = QCoreApplication::applicationFilePath();
    ui->plainTextEdit->appendPlainText(buttonStr + appFilePath);
}

void Dialog::on_pushButton_3_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);

    // QCoreApplication::setApplicationName("MyApp");
    QString appName = QCoreApplication::applicationName();
    ui->plainTextEdit->appendPlainText(buttonStr + appName);
}

void Dialog::on_pushButton_62_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);

    QCoreApplication::setApplicationName("MyApp");
    QString appName = QCoreApplication::applicationName();
    ui->plainTextEdit->appendPlainText(buttonStr + appName);
}

void Dialog::on_pushButton_4_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);

    QStringList libPaths = QCoreApplication::libraryPaths();

    ui->plainTextEdit->appendPlainText(buttonStr);
    for (const QString &path : libPaths)
        ui->plainTextEdit->appendPlainText(path);
}

void Dialog::on_pushButton_61_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);

    QCoreApplication::setOrganizationName("JackWang");
    QString str = QCoreApplication::organizationName();
    ui->plainTextEdit->appendPlainText(buttonStr + "\n" + str);
}

void Dialog::on_pushButton_40_clicked()
{
    QCoreApplication::exit();
}

void Dialog::on_pushButton_48_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString srcFileDir = info.path();
    QString dstFilePath = info.path() + "/" + info.baseName() + "--副本." + info.suffix();

    QFile::copy(srcFilePath, dstFilePath);
    ui->plainTextEdit->appendPlainText("源文件:" + srcFilePath);
    ui->plainTextEdit->appendPlainText("副本文件:" + dstFilePath);
}

void Dialog::on_pushButton_53_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString dstFilePath = info.path() + "/" + info.baseName() + "--副本." + info.suffix();

    QFile srcFile(srcFilePath);
    srcFile.copy(dstFilePath);

    ui->plainTextEdit->appendPlainText("源文件:" + srcFilePath);
    ui->plainTextEdit->appendPlainText("副本文件:" + dstFilePath);
}

void Dialog::on_pushButton_51_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();

    bool exists = QFile::exists(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + (exists ? "存在" : "不存在"));
}

void Dialog::on_pushButton_54_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();

    QFile file(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + (file.exists() ? "存在" : "不存在"));
}

void Dialog::on_pushButton_49_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();

    if (QFile::exists(srcFilePath))
    {
        QFile::remove(srcFilePath);
        ui->plainTextEdit->appendPlainText("删除文件: " + srcFilePath);
    }
    else
        ui->plainTextEdit->appendPlainText("文件不存在");
}

void Dialog::on_pushButton_55_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFile srcFile(srcFilePath);

    if (srcFile.exists())
    {
        srcFile.remove();
        ui->plainTextEdit->appendPlainText("删除文件: " + srcFilePath);
    }
    else
        ui->plainTextEdit->appendPlainText("文件不存在");
}

void Dialog::on_pushButton_50_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString srcFileDir = info.path();
    QString dstFilePath = info.path() + "/" + info.baseName() + "--重命名." + info.suffix();

    QFile::rename(srcFilePath, dstFilePath);
    ui->plainTextEdit->appendPlainText("源文件:" + srcFilePath);
    ui->plainTextEdit->appendPlainText("重命名:" + dstFilePath);
}

void Dialog::on_pushButton_56_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString dstFilePath = info.path() + "/" + info.baseName() + "--重命名." + info.suffix();

    QFile srcFile(srcFilePath);
    srcFile.rename(dstFilePath);

    ui->plainTextEdit->appendPlainText("源文件:" + srcFilePath);
    ui->plainTextEdit->appendPlainText("重命名:" + dstFilePath);
}

void Dialog::on_pushButton_63_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();

    if (QFile::exists(srcFilePath))
    {
        QFile::moveToTrash(srcFilePath);
        ui->plainTextEdit->appendPlainText("文件移动至回收站: " + srcFilePath);
    }
    else
        ui->plainTextEdit->appendPlainText("文件不存在");
}

void Dialog::on_pushButton_64_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFile srcFile(srcFilePath);

    if (srcFile.exists())
    {
        srcFile.moveToTrash();
        ui->plainTextEdit->appendPlainText("文件移动至回收站: " + srcFilePath);
    }
    else
        ui->plainTextEdit->appendPlainText("文件不存在");
}

void Dialog::on_pushButton_28_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.absoluteFilePath();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_29_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.absolutePath();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_33_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.fileName();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_34_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.filePath();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_38_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    qint64 fileSize = info.size();

    ui->plainTextEdit->appendPlainText(QString::asprintf("%s, 文件大小: %lld Bytes", srcFilePath.toStdString().c_str(), fileSize));
}

void Dialog::on_pushButton_37_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.path();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_30_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.baseName();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_31_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.completeBaseName();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_39_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.suffix();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_32_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);
    QString str = info.completeSuffix();

    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_42_clicked()
{

    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcDirPath = ui->editDir->text();
    QFileInfo info(srcDirPath);

    ui->plainTextEdit->appendPlainText(srcDirPath + (info.isDir() ? "是目录" : "不是目录"));
}

void Dialog::on_pushButton_43_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + (info.isDir() ? "是文件" : "不是文件"));
}

void Dialog::on_pushButton_35_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + (info.isExecutable() ? "是可执行文件" : "不是可执行文件"));
}

void Dialog::on_pushButton_58_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + info.birthTime().toString("yyyy-MM-dd hh:mm:ss"));
}

void Dialog::on_pushButton_36_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + info.lastModified().toString("yyyy-MM-dd hh:mm:ss"));
}

void Dialog::on_pushButton_44_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + info.lastRead().toString("yyyy-MM-dd hh:mm:ss"));
}

void Dialog::on_pushButton_59_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    // QFileInfo info(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + (QFileInfo::exists(srcFilePath) ? "存在" : "不存在"));
}

void Dialog::on_pushButton_27_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString srcFilePath = ui->editFile->text();
    QFileInfo info(srcFilePath);

    ui->plainTextEdit->appendPlainText(srcFilePath + (info.exists() ? "存在" : "不存在"));
}

void Dialog::on_pushButton_10_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText(QDir::tempPath());
}

void Dialog::on_pushButton_9_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText(QDir::rootPath());
}

void Dialog::on_pushButton_8_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText(QDir::homePath());
}

void Dialog::on_pushButton_7_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    for (const QFileInfo &info : QDir::drives())
        ui->plainTextEdit->appendPlainText(info.path());
}

void Dialog::on_pushButton_6_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText(QDir::currentPath());
}

void Dialog::on_pushButton_60_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir::setCurrent(ui->editDir->text());
    ui->plainTextEdit->appendPlainText(QDir::currentPath());
}

void Dialog::on_pushButton_20_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString subDir = "subdir1";
    QDir dir(ui->editDir->text());

    bool ok = dir.mkdir(subDir);
    ui->plainTextEdit->appendPlainText(QString("创建目录") + (ok ? "成功" : "失败"));
}

void Dialog::on_pushButton_24_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString subDir = "subdir1";
    QDir dir(ui->editDir->text());

    bool ok = dir.rmdir(subDir);
    ui->plainTextEdit->appendPlainText(QString("删除目录") + (ok ? "成功" : "失败"));
}

void Dialog::on_pushButton_22_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QString file = ui->editFile->text();

    bool ok = dir.remove(file);
    ui->plainTextEdit->appendPlainText(QString("删除文件") + (ok ? "成功" : "失败"));
}

void Dialog::on_pushButton_23_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QString srcFilePath = ui->editFile->text();
    QFileInfo fileInfo(srcFilePath);
    QString dstFilePath = fileInfo.path() + "/" + fileInfo.baseName() + ".XYZ";

    dir.rename(srcFilePath, dstFilePath);
    ui->plainTextEdit->appendPlainText("源文件: " + srcFilePath);
    ui->plainTextEdit->appendPlainText("重命名为: " + dstFilePath);
}

void Dialog::on_pushButton_26_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString currDir = QDir::currentPath();
    QDir lastDir(currDir);
    ui->plainTextEdit->appendPlainText("选择目录之前: " + lastDir.absolutePath());

    QString newDir = QFileDialog::getExistingDirectory(this, "选择一个目录", currDir, QFileDialog::ShowDirsOnly);
    if (newDir.isEmpty())
        return;

    ui->editDir->setText(newDir);
    lastDir.setPath(newDir);
    ui->plainTextEdit->appendPlainText("选择目录之后: " + lastDir.absolutePath());
}

void Dialog::on_pushButton_12_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    bool ok = dir.removeRecursively();
    ui->plainTextEdit->appendPlainText(QString("删除目录及文件") + (ok ? "成功" : "失败"));
}

void Dialog::on_pushButton_13_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QString str = dir.absoluteFilePath(ui->editFile->text());
    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_14_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QString str = dir.absolutePath();
    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_15_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QString str = dir.canonicalPath();
    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_19_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QString str = dir.filePath(ui->editFile->text());
    ui->plainTextEdit->appendPlainText(str);
}

void Dialog::on_pushButton_65_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    ui->plainTextEdit->appendPlainText(dir.path());
}

void Dialog::on_pushButton_16_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    ui->plainTextEdit->appendPlainText(dir.dirName());
}

void Dialog::on_pushButton_18_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    ui->plainTextEdit->appendPlainText(QString("目录") + (dir.exists() ? "存在" : "不存在"));
}

void Dialog::on_pushButton_66_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    ui->plainTextEdit->appendPlainText(QString("目录") + (dir.isEmpty() ? "为空" : "非空"));
}

void Dialog::on_pushButton_11_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QStringList strList = dir.entryList(QDir::Dirs | QDir::NoDotAndDotDot);

    ui->plainTextEdit->appendPlainText("所选目录下的所有目录");
    for (const auto &item : strList)
        ui->plainTextEdit->appendPlainText(item);
}

void Dialog::on_pushButton_17_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QDir dir(ui->editDir->text());
    QStringList strList = dir.entryList(QDir::Files);

    ui->plainTextEdit->appendPlainText("所选目录下的所有文件");
    for (const auto &item : strList)
        ui->plainTextEdit->appendPlainText(item);
}

void Dialog::on_pushButton_21_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText("QDir::tempPath(): " + QDir::tempPath());

    QTemporaryDir dir;
    dir.setAutoRemove(true);
    ui->plainTextEdit->appendPlainText(dir.path());
    ui->plainTextEdit->appendPlainText(QString::asprintf("%d", QDir(dir.path()).exists()));
}

void Dialog::on_pushButton_25_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText("QDir::tempPath(): " + QDir::tempPath());

    QTemporaryFile file;
    file.setAutoRemove(true);
    file.open();
    ui->plainTextEdit->appendPlainText(file.fileName());
    ui->plainTextEdit->appendPlainText(QString::asprintf("%d", QFile(file.fileName()).exists()));
    file.close();
}

void Dialog::on_pushButton_67_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString dir = ui->editDir->text();
    ui->plainTextEdit->appendPlainText("指定的目录: " + dir);

    QTemporaryDir tempDir(dir + "/TempDir_XXXXXX");
    tempDir.setAutoRemove(false);
    ui->plainTextEdit->appendPlainText(tempDir.path());
}

void Dialog::on_pushButton_69_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    QString dir = ui->editDir->text();
    ui->plainTextEdit->appendPlainText("指定的目录: " + dir);

    QTemporaryFile tempFile(dir + "TempFile_XXXXXX.temp");
    tempFile.setAutoRemove(false);
    tempFile.open();
    ui->plainTextEdit->appendPlainText(tempFile.fileName());
    tempFile.close();
}

void Dialog::on_pushButton_68_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText("当前目录: " + QDir::currentPath());

    QTemporaryDir tempDir("SubDir_XXXXXX");
    tempDir.setAutoRemove(false);
    ui->plainTextEdit->appendPlainText(tempDir.path());
}

void Dialog::on_pushButton_70_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    ui->plainTextEdit->appendPlainText("当前目录: " + QDir::currentPath());

    QTemporaryFile tempFile("CurrTempFile_XXXXXX.temp");
    tempFile.setAutoRemove(false);
    tempFile.open();
    ui->plainTextEdit->appendPlainText(tempFile.fileName());
    tempFile.close();
}

void Dialog::on_pushButton_46_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    watcher->addPath(ui->editDir->text());
    watcher->addPath(ui->editFile->text());

    connect(watcher, &QFileSystemWatcher::directoryChanged, this, &Dialog::do_directoryChanged);
    connect(watcher, &QFileSystemWatcher::fileChanged, this, &Dialog::do_fileChanged);
}

void Dialog::on_pushButton_47_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    watcher->removePath(ui->editDir->text());
    watcher->removePath(ui->editFile->text());

    disconnect(watcher);
}

void Dialog::on_pushButton_52_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    for (auto &item : watcher->directories())
        ui->plainTextEdit->appendPlainText(item);
}

void Dialog::on_pushButton_57_clicked()
{
    QPushButton *button = dynamic_cast<QPushButton *>(sender());
    QString buttonStr = getButtonStr(button);
    ui->plainTextEdit->appendPlainText(buttonStr);

    for (auto &item : watcher->files())
        ui->plainTextEdit->appendPlainText(item);
}
