//
// Created by Aurelian on 06/04/2022.
//

#include "ui.h"
#include <iostream>

using namespace std;

UI::UI(Service *service1) {
    this->service = service1;
}

void UI::printMenu() {
    cout << "Menu" << endl;
    cout << "0.Exit" << endl;
    cout << "1.Remove an element" << endl;
    cout << "2.Print all "<< endl;
    cout << "3.Print sorted and filtered" << endl;
}

void UI::start() {
    bool done = false;

    while(!done)
    {
        try{
            printMenu();
            string option;
            getline(cin, option);
            if(option == "0")
                done = true;
            else if(option == "1")
                this->removeUI();
            else if(option == "2")
                this->printAll();
            else if(option == "3")
                this->printSorted();
            else
                cout << "Invalid command!";
        }
        catch(const char* msg)
        {
            cout << msg << endl;
        }
        catch(const exception & e)
        {
            cout << e.what() << endl;
        }


    }


}

void UI::removeUI() {
    string organism, name;

    cout << "Organism: " << endl;
    getline(cin, organism);

    cout << "Name: " << endl;
    getline(cin, name);

    int removed = this->service->removeService(organism, name);

    if(removed == 0)
        throw "The protein isn t in the database";
    else
        cout << "Protein successfully removed!";

}

void UI::printAll() {
    Protein* proteins = this->service->getAllService();

    int length = this->service->getSizeService();

    for(int i = 0; i < length; i++)
        cout << i+1 << ". " << proteins[i].toString() << endl;

}

void UI::printSorted() {
    auto result = new Protein[this->service->getSizeService()];

    string sequence;

    cout << "Sequence: " << endl;
    getline(cin, sequence);

    int filtered = this->service->filter(sequence, result);

    if(filtered == 0)
        throw "No matches found";

    for(int i = 0; i < filtered; i++)
        cout << i+1 << ". " << result[i].toString() << endl;

}

