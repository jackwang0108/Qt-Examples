#include <QSpinBox>

#include "tspinboxdelegate.h"

TSpinboxDelegate::TSpinboxDelegate(QObject *parent)
    : QStyledItemDelegate(parent)
{
}

QWidget *TSpinboxDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(option);
    Q_UNUSED(index);

    QSpinBox *editor = new QSpinBox(parent);
    editor->setFrame(false);
    editor->setMinimum(0);
    editor->setMaximum(500000);
    return editor;
}

void TSpinboxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    QSpinBox *spinbox = dynamic_cast<QSpinBox *>(editor);

    int value = index.model()->data(index, Qt::EditRole).toInt();
    spinbox->setValue(value);
}

void TSpinboxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    QSpinBox *spinbox = dynamic_cast<QSpinBox *>(editor);

    int value = spinbox->value();
    model->setData(index, value, Qt::EditRole);
}

void TSpinboxDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(index);
    editor->setGeometry(option.rect);
}
