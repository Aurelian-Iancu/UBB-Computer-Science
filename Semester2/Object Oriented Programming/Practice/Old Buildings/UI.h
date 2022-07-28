#pragma once

#include "Service.h"

class UI{
private:
    Service service;

public:
    UI(Service service1);

    void printMenu();

    void run();

    void addBuilding();

    void showAll();

    void showAllRestored();

    void saveFile();

    void initialiseList();
};