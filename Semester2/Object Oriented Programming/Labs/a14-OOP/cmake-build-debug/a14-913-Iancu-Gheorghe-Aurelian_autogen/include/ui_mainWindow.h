/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_mainWindow
{
public:
    QListWidget *shoppingListWidget;
    QPushButton *pushButton;
    QLabel *label;
    QLineEdit *lineEdit;

    void setupUi(QWidget *mainWindow)
    {
        if (mainWindow->objectName().isEmpty())
            mainWindow->setObjectName(QString::fromUtf8("mainWindow"));
        mainWindow->resize(979, 539);
        shoppingListWidget = new QListWidget(mainWindow);
        shoppingListWidget->setObjectName(QString::fromUtf8("shoppingListWidget"));
        shoppingListWidget->setGeometry(QRect(290, 10, 371, 192));
        pushButton = new QPushButton(mainWindow);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(250, 410, 83, 29));
        label = new QLabel(mainWindow);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(390, 310, 63, 20));
        lineEdit = new QLineEdit(mainWindow);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(500, 310, 113, 28));

        retranslateUi(mainWindow);

        QMetaObject::connectSlotsByName(mainWindow);
    } // setupUi

    void retranslateUi(QWidget *mainWindow)
    {
        mainWindow->setWindowTitle(QCoreApplication::translate("mainWindow", "mainWindow", nullptr));
        pushButton->setText(QCoreApplication::translate("mainWindow", "PushButton", nullptr));
        label->setText(QCoreApplication::translate("mainWindow", "TextLabel", nullptr));
    } // retranslateUi

};

namespace Ui {
    class mainWindow: public Ui_mainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
