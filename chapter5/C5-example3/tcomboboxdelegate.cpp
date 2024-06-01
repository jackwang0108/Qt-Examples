#include <QComboBox>

#include "tcomboboxdelegate.h"

TComboBoxDelegate::TComboBoxDelegate(QObject *parent)
    : QStyledItemDelegate{parent}
{
}

QWidget *TComboBoxDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(option);
    Q_UNUSED(index);

    QComboBox *combo = new QComboBox(parent);
    combo->setEditable(editable);

    for (const auto &item : itemList)
        combo->addItem(item);

    return combo;
}

void TComboBoxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    QComboBox *combo = dynamic_cast<QComboBox *>(editor);

    QString str = index.model()->data(index, Qt::EditRole).toString();

    combo->setCurrentText(str);
}

void TComboBoxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    QComboBox *combo = dynamic_cast<QComboBox *>(editor);

    QString str = combo->currentText();
    model->setData(index, str, Qt::EditRole);
}

void TComboBoxDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(index);

    QComboBox *combo = dynamic_cast<QComboBox *>(editor);
    combo->setGeometry(option.rect);
}

void TComboBoxDelegate::setItem(QStringList item, bool editable)
{
    itemList = item;
    editable = editable;
}