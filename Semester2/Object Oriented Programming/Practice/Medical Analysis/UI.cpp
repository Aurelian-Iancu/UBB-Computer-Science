//
// Created by Aurelian on 03/05/2022.
//

#include "UI.h"
#include "iostream"
#include "Person.h"

UI::UI(Person &p): p{p} {

}

void UI::run() {
    while (true)
    {
        int option;
        std::cout << "0. Exit\n";
        std::cout << "1. Show all analyses\n";
        std::cout << "2. Save to file all analyses between two given dates\n";
        std::cin >> option;
        if (option == 0)
        {
            return;
        }
        else if (option == 1)
        {
            for (auto e : this->p.getAllAnalysis())
            {
                std::cout << e->toString() << '\n';
            }
        }
        else if (option == 2)
        {

        }
    }
}

