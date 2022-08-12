#pragma once

#include "service.h"

class UI{
private:
    Service* service;

public:
    explicit UI(Service* service1);

    ~UI() = default;

    void addUI();

    void printMenu();

    void start();

    void printAll();

    void printSorted();
};
