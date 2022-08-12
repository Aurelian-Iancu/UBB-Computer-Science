/********************************************************************************
** Form generated from reading UI file 'window.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WINDOW_H
#define UI_WINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Window
{
public:
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout;
    QListWidget *issueListWidget;
    QVBoxLayout *verticalLayout_2;
    QGridLayout *gridLayout_3;
    QLabel *label_2;
    QLineEdit *removeLineEdit;
    QPushButton *removePushButton;
    QGridLayout *gridLayout;
    QPushButton *addPushButton;
    QLineEdit *addLineEdit;
    QLabel *label;
    QGridLayout *gridLayout_4;
    QLabel *label_3;
    QPushButton *resolvePushButton;

    void setupUi(QWidget *Window)
    {
        if (Window->objectName().isEmpty())
            Window->setObjectName(QString::fromUtf8("Window"));
        Window->resize(1226, 582);
        horizontalLayoutWidget = new QWidget(Window);
        horizontalLayoutWidget->setObjectName(QString::fromUtf8("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(180, 10, 761, 561));
        horizontalLayout = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        issueListWidget = new QListWidget(horizontalLayoutWidget);
        issueListWidget->setObjectName(QString::fromUtf8("issueListWidget"));

        horizontalLayout->addWidget(issueListWidget);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        label_2 = new QLabel(horizontalLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_3->addWidget(label_2, 1, 0, 1, 1);

        removeLineEdit = new QLineEdit(horizontalLayoutWidget);
        removeLineEdit->setObjectName(QString::fromUtf8("removeLineEdit"));

        gridLayout_3->addWidget(removeLineEdit, 1, 1, 1, 1);

        removePushButton = new QPushButton(horizontalLayoutWidget);
        removePushButton->setObjectName(QString::fromUtf8("removePushButton"));

        gridLayout_3->addWidget(removePushButton, 2, 1, 1, 1);


        verticalLayout_2->addLayout(gridLayout_3);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        addPushButton = new QPushButton(horizontalLayoutWidget);
        addPushButton->setObjectName(QString::fromUtf8("addPushButton"));

        gridLayout->addWidget(addPushButton, 2, 1, 1, 1);

        addLineEdit = new QLineEdit(horizontalLayoutWidget);
        addLineEdit->setObjectName(QString::fromUtf8("addLineEdit"));

        gridLayout->addWidget(addLineEdit, 1, 1, 1, 1);

        label = new QLabel(horizontalLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 1, 0, 1, 1);


        verticalLayout_2->addLayout(gridLayout);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        label_3 = new QLabel(horizontalLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout_4->addWidget(label_3, 0, 0, 1, 1);

        resolvePushButton = new QPushButton(horizontalLayoutWidget);
        resolvePushButton->setObjectName(QString::fromUtf8("resolvePushButton"));

        gridLayout_4->addWidget(resolvePushButton, 0, 1, 1, 1);


        verticalLayout_2->addLayout(gridLayout_4);


        horizontalLayout->addLayout(verticalLayout_2);


        retranslateUi(Window);

        QMetaObject::connectSlotsByName(Window);
    } // setupUi

    void retranslateUi(QWidget *Window)
    {
        Window->setWindowTitle(QCoreApplication::translate("Window", "Window", nullptr));
        label_2->setText(QCoreApplication::translate("Window", "Remove", nullptr));
        removePushButton->setText(QCoreApplication::translate("Window", "Remove", nullptr));
        addPushButton->setText(QCoreApplication::translate("Window", "Add", nullptr));
        label->setText(QCoreApplication::translate("Window", "Add", nullptr));
        label_3->setText(QCoreApplication::translate("Window", "Resolve", nullptr));
        resolvePushButton->setText(QCoreApplication::translate("Window", "Resolve", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Window: public Ui_Window {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WINDOW_H
