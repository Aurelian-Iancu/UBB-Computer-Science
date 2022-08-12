#pragma once

#include "service.h"

class UI{
private:
    Service* service;
public:
    UI(Service* service1);

    ~UI() = default;

    void printMenu();

    void start();

    void removeUI();

    void printAll();

    void printSorted();
};
