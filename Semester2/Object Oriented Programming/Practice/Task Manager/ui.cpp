

#include "ui.h"
#include <iostream>
using namespace std;


UI::UI(Service *service1) {
    this->service = service1;
}

void UI::printMenu() {
    cout << "Menu" << endl;
    cout << "0. Exit" << endl;
    cout << "1. If you want to add a task" << endl;
    cout << "2. If you want to print the list of tasks" << endl;
    cout << "3. If you want to print them filtered and sorted" << endl;
}
void UI::addUI() {
    string description, durationS, priorityS;
    int duration, priority;

    cout << "Description: " << endl;
    getline(cin, description);

    cout << "Duration: " << endl;
    getline(cin, durationS);

    duration = stoi(durationS);

    cout << "Priority: " << endl;
    getline(cin, priorityS);

    priority = stoi(priorityS);

    int added = this->service->addService(description, duration, priority);

    if(added == 1)
        throw "The task is already in the database";
    else
        cout << "Task successfully added!" << endl;
}

void UI::printAll() {
    Task* tasks = this->service->getAllService();

    int length = this->service->getSizeService();

    for(int i = 0; i < length; i++)
    {
        cout << i+1 << ". " << tasks[i].toString() << endl;
    }
}

void UI::printSorted() {
    auto result = new Task[this->service->getSizeService()];
    string priorityS;
    int priority;

    cout << "Priority: " << endl;
    getline(cin, priorityS);

    priority = stoi(priorityS);

    int filtered = this->service->filtered(priority, result);

    if(filtered == 0)
        throw "No match found";
    else
        for(int i = 0; i < filtered ;i++)
            cout << i+1 << ". " << result[i].toString() << endl;


}

void UI::start() {
    bool done = false;

    while(!done)
    {
        printMenu();
        string option;
        getline(cin, option);
        try{
        if(option == "0")
            done = true;
        else if(option == "1")
            this->addUI();
        else if(option == "2")
            this->printAll();
        else if(option == "3")
            this->printSorted();
        else
            cout << "Invalid command!" << endl;
        }
        catch(const char* msg) { cout << msg << endl; }
        catch(const exception& exception)
        {
            cout << exception.what() << endl;
        }
    }
}





