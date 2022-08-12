//
// Created by Aurelian on 04/06/2022.
//

#ifndef COURSEEXAMPLE_WINDOW_H
#define COURSEEXAMPLE_WINDOW_H

#include <QWidget>
#include "service.h"
#include "Observer.h"


QT_BEGIN_NAMESPACE
namespace Ui { class Window; }
QT_END_NAMESPACE

class Window : public QWidget, public Observer {
Q_OBJECT

public:
    explicit  Window(Service& service,User* user, QWidget *parent = nullptr);

    ~Window() override;

    void populateList();

    void connectSignalsAndSlots();

    void addIssue();

    void removeIssue();

    void resolveIssue();

    void update() override;

    void lockResolveButton();


private:
    Ui::Window *ui;
    Service& service;
    User* user;
};


#endif //COURSEEXAMPLE_WINDOW_H
