#include "ui.h"

#include <iostream>

using namespace std;

UI::UI(Service *service1) {
    this->service = service1;
}

void UI::printMenu()
{
    cout << "\t\t Menu" << endl;
    cout << "0. Exit" << endl;
    cout << "1. To add a player" << endl;
    cout << "2. To print all players" << endl;
    cout << "3. To print all players from a given team sorted" << endl;
}

void UI::addUI() {
    string name, nationality, team, nOfGoalsS;
    int nOfGoals;

    cout << "Name: " << endl;
    getline(cin, name);

    cout << "Nationality: "<< endl;
    getline(cin, nationality);

    cout << "Team: " << endl;
    getline(cin, team);

    cout <<"Number of goals: " << endl;
    getline(cin, nOfGoalsS);
    nOfGoals = stoi(nOfGoalsS);

    int added = this->service->addService(name, nationality, team, nOfGoals);

    if(added == 1)
        throw "The player is already in the database";
    else if(added == 0)
        cout << "Player was successfully added!" << endl;
}

void UI::printAll()
{
    TopScorer* topScorer = this->service->getAllService();
    int nrElements = this->service->getSizeService();
    if(nrElements == 0)
        throw "The repository is empty";
    for(int i = 0; i < nrElements; i++)
        cout << i+1 << ". " << topScorer[i].toString() << endl;
}

void UI::printSorted()
{
    auto result = new TopScorer[this->service->getSizeService()];

    string team;
    cout << "Enter team: " << endl;
    getline(cin, team);

    int filtered;
    filtered = this->service->filter(team, result);

    if(filtered == 0)
        throw "There are no players in that team";

    for(int i = 0; i < filtered; i++)
        cout << i+1 << ". " << result[i].toString() << endl;


}


void UI::start()
{
    bool running = true;

    while(running)
    {
        try
        {
            printMenu();
            string option;
            getline(cin, option);

            if (option == "1")
                this->addUI();
            else if(option == "2")
                this->printAll();
            else if(option == "3")
                this->printSorted();
            else if(option == "0")
                running = false;
            else
                cout << "Invalid command! Try again!" << endl;
        }
        catch(const char* msg)
        {
            cout << msg << endl;
        }
        catch(const exception& e)
        {
            cout << e.what() << endl;
            cout << endl;
        }

    }
}
