

#include "UI.h"
#include <iostream>
#include "Surgery.h"
#include "NeonatalUnit.h"

using namespace std;

UI::UI(Service &service): service(service){}

void UI::printMenu() {
    cout << "0. Exit\n";
    cout << "1. Add department\n";
    cout << "2. Show all\n";
    cout << "3. Show efficient\n";
    cout << "4. Save to file\n";
}

void UI::run()
{
    string option;
    this->initialise();
    while(true)
    {
        this->printMenu();
        cin>>option;
        if(option == "0")
            break;
        else if(option == "1")
            this->addDepartament();
        else if(option == "2")
            this->showAll();
        else if(option == "3")
            this->showAllEfficient();
        else if(option == "4")
            this->save();
    }
}

void UI::initialise() {
    HospitalDepartment* hospitalDepartment;

    auto a = new Surgery("Regina Maria3", 10, 25);

    hospitalDepartment = a;
    this->service.addDepartment(hospitalDepartment);

    auto b = new Surgery("Regina Maria2", 15, 15);

    hospitalDepartment = b;
    this->service.addDepartment(hospitalDepartment);

    auto c = new NeonatalUnit("Regina Maria5", 10, 25, 26, 1.6);

    hospitalDepartment = c;
    this->service.addDepartment(hospitalDepartment);

    auto d = new NeonatalUnit("Regina Maria51", 15, 15, 15, 1.2);

    hospitalDepartment = d;
    this->service.addDepartment(hospitalDepartment);

}

void UI::showAll() {
    for(auto &i: this->service.getAll())
    {
        cout << i->toString() << endl;
    }
}

void UI::addDepartament() {
    string type;
    cout << "Type(NeonatalUnit or surgery)";
    cin >> type;
    if(type == "neo")
    {
        string hospitalName;
        int doctors, moms, newborns;
        double averageGrade;

        cout << "Hospital name";
        cin >> hospitalName;
        cout << "doctors";
        cin >> doctors;
        cout << "Moms";
        cin >> moms;
        cout << "Newborns";
        cin >> newborns;
        cout << "average grade";
        cin >> averageGrade;

        HospitalDepartment* a;

        auto b = new NeonatalUnit(hospitalName, doctors, moms, newborns, averageGrade);

        a = b;
        this->service.addDepartment(a);
    }
    else if(type == "surgery")
    {
        string hospitalName;
        int doctors, patients;


        cout << "Hospital name";
        cin >> hospitalName;
        cout << "doctors";
        cin >> doctors;
        cout << "patients";
        cin >> patients;

        HospitalDepartment* a;

        auto b = new Surgery(hospitalName, doctors, patients);

        a = b;
        this->service.addDepartment(a);
    }
}

void UI::showAllEfficient() {
    for(auto &i: this->service.getAllEfficient())
    {
        cout << i->toString() << endl;
    }
}

void UI::save() {
    string filename;
    cout << "Filename: ";
    cin >> filename;
    this->service.writeToFile(filename);
}

