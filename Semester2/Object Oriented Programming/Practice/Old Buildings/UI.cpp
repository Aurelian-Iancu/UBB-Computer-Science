

#include "UI.h"
#include <iostream>

using namespace std;

UI::UI(Service service1):service{service1}{

}

void UI::printMenu() {
    cout << "0. Exit\n";
    cout << "1. Add a new building\n";
    cout << "2. Show all buildings\n";
    cout << "3. Show all buildings that must be restored\n";
    cout << "4. Save\n";

}

void UI::run() {
    std::string option;
    this->initialiseList();
    while(true)
    {
        this->printMenu();
        cin >> option;
        if(option == "0")
            break;
        else if(option == "1")
            this->addBuilding();
        else if(option == "2")
            this->showAll();
        else if(option == "3")
            this->showAllRestored();
        else if(option == "4")
            this->saveFile();
    }
}

void UI::addBuilding() {
    string type;
    cout << "What type of building? block or house";
    cin >> type;
    if(type == "house")
    {
        int year;
        string address, historical;
        cout << "Year";
        cin >> year;
        cout << "Address";
        cin >> address;
        cout << "Historical yes or no";
        cin >> historical;
        bool bHistorical;
        if(historical == "yes")
            bHistorical = true;
        else
            bHistorical = false;
        Building* a;
        auto b = new House(address, year, bHistorical);
        a = b;
        this->service.addBuilding(a);
    }
    else if(type == "block"){
        int year, total, occupied;
        string address;
        cout << "Year";
        cin >> year;
        cout << "Address";
        cin >> address;
        cout << "Total";
        cin >> total;
        cout << "Occupied";
        cin >> occupied;
        Building* a;
        auto b = new Block(address, year, total, occupied);
        a = b;
        this->service.addBuilding(a);
    }
}

void UI::showAll() {
    for(auto &i: this->service.getAllBuildings())
    {
        cout << i->toString() << endl;
    }

}

void UI::showAllRestored() {
    vector<Building*> help;
    int Year;
    cout << "Year";
    cin >> Year;
    for(auto &i: this->service.getAllToBeRestored())
    {
        if(i->getYear() < Year)
        {
            help.push_back(i);
        }
    }

    for(auto &i: help)
        cout << i->toString() << endl;
}

void UI::saveFile() {
    string fileForRestored, fileForDemolished;
    cout << "File for restored";
    cin >> fileForRestored;
    cout << "File for demolished";
    cin >> fileForDemolished;
    auto a = this->service.getAllToBeRestored();
    this->service.writeToFile(fileForRestored, a);

    auto c = this->service.getAllToBeDemolished();
    this->service.writeToFile(fileForDemolished, c);
}

void UI::initialiseList() {
    Building* a;

    auto b = new Block("idk", 1900, 200, 45);
    a = b;
    this->service.addBuilding(a);

    auto c = new Block("awfasasf", 143, 3140, 3012);
    a = c;
    this->service.addBuilding(a);

    auto d = new House("wge earh", 1502, true);
    a = d;
    this->service.addBuilding(a);

    auto e = new House("wge waf earh", 1572, false);
    a = e;
    this->service.addBuilding(a);
}
