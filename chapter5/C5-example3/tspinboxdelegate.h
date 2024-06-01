#ifndef TSPINBOXDELEGATE_H
#define TSPINBOXDELEGATE_H

#include <QObject>
#include <QStyledItemDelegate>

class TSpinboxDelegate : public QStyledItemDelegate
{
    Q_OBJECT
public:
    explicit TSpinboxDelegate(QObject *parent = nullptr);

    // QAbstractItemDelegate interface
public:
    virtual QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const override;
    virtual void setEditorData(QWidget *editor, const QModelIndex &index) const override;
    virtual void setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const override;
    virtual void updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const override;
};

#endif // TSPINBOXDELEGATE_H
