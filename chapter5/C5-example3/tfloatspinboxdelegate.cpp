#include <QDoubleSpinBox>

#include "tfloatspinboxdelegate.h"

TFloatSpinboxDelegate::TFloatSpinboxDelegate(QObject *parent)
    : QStyledItemDelegate{parent}
{
}

QWidget *TFloatSpinboxDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(option);
    Q_UNUSED(index);

    QDoubleSpinBox *editor = new QDoubleSpinBox(parent);
    editor->setFrame(false);
    editor->setMinimum(0);
    editor->setMaximum(500000);
    editor->setSingleStep(0.1);
    return editor;
}

void TFloatSpinboxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    QDoubleSpinBox *spin = dynamic_cast<QDoubleSpinBox *>(editor);

    double value = index.model()->data(index, Qt::EditRole).toDouble();
    spin->setValue(value);
}

void TFloatSpinboxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    QDoubleSpinBox *spin = dynamic_cast<QDoubleSpinBox *>(editor);

    double value = spin->value();
    model->setData(index, value, Qt::EditRole);
}

void TFloatSpinboxDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(index);

    QDoubleSpinBox *spin = dynamic_cast<QDoubleSpinBox *>(editor);
    spin->setGeometry(option.rect);
}
