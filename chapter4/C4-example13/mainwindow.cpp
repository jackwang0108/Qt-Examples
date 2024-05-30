#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->treeWidget->clear();

    // 设置TreeWidget表头
    setupTreeWidgetHeader({"目录和文件", "节点类型", "最后的修改日期"});
    // 添加一个根节点
    QIcon icon(":/images/icons/15.ico");
    QTreeWidgetItem *topItem = new QTreeWidgetItem(itTopItem);
    topItem->setIcon(colItem, icon);
    topItem->setText(colItem, "图片");
    topItem->setText(colItemType, "Top Item");
    topItem->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
    topItem->setCheckState(colItem, Qt::Checked);
    ui->treeWidget->addTopLevelItem(topItem);

    // 状态栏
    labelNodeText = new QLabel("节点标题", this);
    labelNodeText->setMinimumWidth(200);
    ui->statusbar->addWidget(labelNodeText);

    scaleRatio = new QSpinBox(this);
    scaleRatio->setRange(0, 2000);
    scaleRatio->setValue(100);
    scaleRatio->setSuffix(" %");
    scaleRatio->setReadOnly(true);
    scaleRatio->setButtonSymbols(QAbstractSpinBox::NoButtons);
    ui->statusbar->addPermanentWidget(scaleRatio);

    labelFileName = new QLabel("文件名", this);
    ui->statusbar->addWidget(labelFileName);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setupTreeWidgetHeader(QStringList strList)
{
    QTreeWidgetItem *header = new QTreeWidgetItem;
    for (int i = 0; i < strList.size(); i++)
        header->setText(i, strList[i]);

    header->setTextAlignment(treeColumn::colItem, Qt::AlignHCenter | Qt::AlignVCenter);
    header->setTextAlignment(treeColumn::colItemType, Qt::AlignHCenter | Qt::AlignVCenter);

    ui->treeWidget->setHeaderItem(header);
}

void MainWindow::on_actAddDir_triggered()
{
    QString dirPath = QFileDialog::getExistingDirectory();
    if (dirPath.isEmpty())
        return;

    QTreeWidgetItem *parentItem = ui->treeWidget->currentItem();
    if (parentItem == nullptr)
        return;

    if (parentItem->type() != itImageItem)
    {
        QTreeWidgetItem *item = new QTreeWidgetItem(itGroupItem);
        QIcon icon(":/images/icons/open3.bmp");

        int length = dirPath.length();
        int lastSlash = dirPath.lastIndexOf("/");
        QString dirName = dirPath.right(length - lastSlash - 1);

        item->setIcon(colItem, icon);
        item->setText(colItem, dirName);
        item->setText(colItemType, "Group Item");
        item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
        item->setCheckState(colItem, Qt::Checked);
        item->setData(colItem, Qt::UserRole, QVariant(dirPath));
        parentItem->addChild(item);
    }
}

void MainWindow::on_actAddFile_triggered()
{
    QStringList filePaths = QFileDialog::getOpenFileNames(this, "选择文件", "", "Images(*.jpg)");

    if (filePaths.isEmpty())
        return;

    QTreeWidgetItem *parentItem = ui->treeWidget->currentItem();

    if (parentItem == nullptr)
        parentItem = ui->treeWidget->topLevelItem(0);
    else
        parentItem = parentItem->type() == itImageItem ? parentItem->parent() : parentItem;

    for (int i = 0; i < filePaths.size(); i++)
    {
        QString filePath = filePaths[i];
        QIcon icon(":/images/icons/31.ico");

        QFileInfo fileInfo(filePath);
        QString fileName = fileInfo.fileName();
        QDateTime fileDateTime = fileInfo.lastModified();

        QTreeWidgetItem *item = new QTreeWidgetItem(itImageItem);
        item->setIcon(colItem, icon);
        item->setText(colItem, fileName);
        item->setText(colItemType, "Image Type");
        item->setText(colDate, fileDateTime.toString("yyyy-MM-dd"));

        item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
        item->setCheckState(colItem, Qt::Checked);
        item->setData(colItem, Qt::UserRole, QVariant(filePath));
        parentItem->addChild(item);
    }

    parentItem->setExpanded(true);
}

void MainWindow::on_actDeleteItem_triggered()
{
    QTreeWidgetItem *currItem = ui->treeWidget->currentItem();

    if (currItem == nullptr || currItem->type() == itTopItem)
        return;

    QTreeWidgetItem *parentItem = currItem->parent();
    parentItem->removeChild(currItem);
}

void MainWindow::on_treeWidget_currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous)
{
    if (current == nullptr || current == previous)
        return;

    switch (current->type())
    {
    case itTopItem:
        ui->actAddDir->setEnabled(true);
        ui->actAddFile->setEnabled(true);
        ui->actDeleteItem->setEnabled(false);
        break;

    case itGroupItem:
        ui->actAddDir->setEnabled(true);
        ui->actAddFile->setEnabled(true);
        ui->actDeleteItem->setEnabled(true);
        break;

    case itImageItem:
        ui->actAddDir->setEnabled(false);
        ui->actAddFile->setEnabled(false);
        ui->actDeleteItem->setEnabled(true);
        displayImage(current);
        break;

    default:
        break;
    }
}

void MainWindow::recursiveChangeCaption(QTreeWidgetItem *curr)
{
    QString str = "*" + curr->text(colItem);

    curr->setText(colItem, str);

    // 宽度优先遍历
    if (curr->childCount() > 0)
        for (int i = 0; i < curr->childCount(); i++)
            recursiveChangeCaption(curr->child(i));
}

void MainWindow::on_actScanItems_triggered()
{
    for (int i = 0; i < ui->treeWidget->topLevelItemCount(); i++)
        recursiveChangeCaption(ui->treeWidget->topLevelItem(i));
}

void MainWindow::on_actZoomFitWidth_triggered()
{
    int picWidth = pixMap.width();
    int areaWidth = ui->scrollArea->width() - 30;

    ratio = float(areaWidth) / picWidth;
    scaleRatio->setValue(ratio * 100);

    QPixmap pix = pixMap.scaledToWidth(areaWidth - 30);
    ui->labelPic->setPixmap(pix);
}

void MainWindow::on_actZoomFitHeight_triggered()
{
    int picHeight = pixMap.height();
    int areaHeight = ui->scrollArea->height() - 30;

    ratio = picHeight / float(areaHeight);
    scaleRatio->setValue(ratio * 100);

    QPixmap pix = pixMap.scaledToHeight(areaHeight - 30);
    ui->labelPic->setPixmap(pix);
}

void MainWindow::displayImage(QTreeWidgetItem *curr)
{
    if (curr->type() != itImageItem)
        return;

    QString fileName = curr->data(colItem, Qt::UserRole).toString();

    QFileInfo fileInfo = QFileInfo(fileName);

    labelFileName->setText("文件名:" + fileInfo.fileName());
    labelNodeText->setText(curr->text(colItem));
    pixMap.load(fileName);
    ui->actZoomFitHeight->triggered();

    ui->actZoomFitHeight->setEnabled(true);
    ui->actZoomFitWidth->setEnabled(true);
    ui->actZoomIn->setEnabled(true);
    ui->actZoomOut->setEnabled(true);
    ui->actRealSize->setEnabled(true);
}
void MainWindow::on_actRealSize_triggered()
{
    ui->labelPic->setPixmap(pixMap);

    ratio = 1;
    scaleRatio->setValue(100);
}

void MainWindow::on_actZoomIn_triggered()
{
    ratio = ratio * 1.2;
    int width = ratio * pixMap.width();
    int height = ratio * pixMap.height();

    ui->labelPic->setPixmap(ui->labelPic->pixmap().scaled(width, height));
    scaleRatio->setValue(ratio * 100);
}

void MainWindow::on_actZoomOut_triggered()
{
    ratio = ratio * 0.8;

    int height = ratio * pixMap.height();

    ui->labelPic->setPixmap(ui->labelPic->pixmap().scaled(width, height));
    scaleRatio->setValue(ratio * 100);
}

void MainWindow::on_actDockVisible_triggered(bool checked)
{
    ui->dockWidget->setVisible(checked);
}

void MainWindow::on_actDockFloat_triggered(bool checked)
{
    ui->dockWidget->setFloating(checked);
}

void MainWindow::on_dockWidget_visibilityChanged(bool visible)
{
    ui->actDockVisible->setChecked(visible);
}

void MainWindow::on_dockWidget_topLevelChanged(bool topLevel)
{
    ui->actDockFloat->setChecked(topLevel);
}
