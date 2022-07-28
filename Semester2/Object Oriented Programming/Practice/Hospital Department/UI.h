#pragma once

#include <string>
#include "Service.h"

class UI{
private:
    Service &service;

public:
    UI(Service &service);

    void printMenu();

    void run();

    void addDepartament();

    void showAll();

    void showAllEfficient();

    void save();

    ~UI() = default;

    void initialise();
};
