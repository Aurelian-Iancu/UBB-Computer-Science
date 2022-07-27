#include "ui.h"
#include <windows.h>
#include <shellapi.h>
#include <iostream>
using namespace std;

UI::UI(Service *service, UserService* userService)
{
    this->service = service;
    this->userService = userService;
}

void UI::printMenuMode()
{
    cout << "1: If you want to enter the admin mode\n";
    cout << "2: If you want to enter the user mode\n";
    cout << "0: if you want to exit the application";
}

void UI::printMenuAdmin(){
    cout << "ADMIN MENU:\n";
    cout << "1. If you want to print all the movies from the database\n";
    cout << "2. If you want to add a movie\n";
    cout << "3. If you want to remove a movie\n";
    cout << "4. If you want to update a movie\n";
    cout << "0. If you want to exit the application\n";
}

void UI::printMenuUser()
{
    cout << "USER MENU:\n";
    cout << "1. To list the movies of a particular gender 1 by 1\n";
    cout << "2. To remove a movie from the playlist\n";
    cout << "3. To list the playlist\n";
    cout << "0. To exit the user mode\n";
}

bool UI::validateString(string input) {
    for (int i = 0; i <input.length(); i++)
        if (isdigit(input[i]) != false)
            return false;
    return true;
}

void UI::addMovieAdmin(){
    cout << "Add a new movie" << endl;
    string title, genre, yearS, numberOfLikesS, trailer;
    int year, numberOfLikes;

    cout << "Enter the title" << endl;
    getline(cin , title);
    if(title.length() == 0)
        throw "Title input not valid";

    cout << "Enter the genre" << endl;
    getline(cin, genre);
    if(genre.length() == 0)
        throw "Genre input not valid";

    cout << "Enter the year of release" << endl;
    getline(cin, yearS);
    if(!(validateString(yearS)) && yearS.length() != 0)
        year = stoi(yearS);
    else
        throw "Year input not valid";
    if(year < 0)
        throw "The year should be a positive number";

    cout << "Enter the number of likes" << endl;
    getline(cin, numberOfLikesS);
    if(!(validateString(numberOfLikesS)) && numberOfLikesS.length() != 0)
        numberOfLikes = stoi(numberOfLikesS);
    else
        throw "Number of likes input not valid";
    if(numberOfLikes < 0)
        throw("The number of likes should be a positive number");

    cout << "Enter link of the trailer" << endl;
    getline(cin, trailer);
    if(trailer.length() == 0)
        throw "Trailer input not valid";

    int added = this->service->addService(title, genre, year, numberOfLikes, trailer);
    if(added == 1)
        throw "This movie is already in the database";
    else if(added == 0)
        cout << "Movie successfully added" << endl;

}

void UI::removeMovieAdmin(){
    cout << "Delete a movie" << endl;
    string title;
    cout << "Enter the title" << endl;
    getline(cin, title);
    if(title.length() == 0)
        throw "Name input not valid";
    int removed = this->service->removeService(title);
    if(removed == 0)
        cout << "Movie successfully removed" << endl;
    else if(removed == 1)
        throw "The movie does not exist in the database";

}

void UI::updateMovieAdmin() {
    cout << "Update a movie" << endl;
    string oldTitle, newTitle, newGenre, newYearS, newNumberOfLikesS, newTrailer;
    int newYear, newNumberOfLikes;

    cout << "Enter the old title" << endl;
    getline(cin , oldTitle);
    if(oldTitle.length() == 0)
        throw "Old title input not valid";

    cout << "Enter the new title" << endl;
    getline(cin , newTitle);
    if(newTitle.length() == 0)
        throw "New title input not valid";

    cout << "Enter the genre" << endl;
    getline(cin, newGenre);
    if(newGenre.length() == 0)
        throw "Genre input not valid";

    cout << "Enter the year of release" << endl;
    getline(cin, newYearS);
    if(!(validateString(newYearS)) && newYearS.length() != 0)
        newYear = stoi(newYearS);
    else
        throw "Year input not valid";
    if(newYear < 0)
        throw "The year should be a positive number";

    cout << "Enter the number of likes" << endl;
    getline(cin, newNumberOfLikesS);
    if(!(validateString(newNumberOfLikesS)) && newNumberOfLikesS.length() != 0)
        newNumberOfLikes = stoi(newNumberOfLikesS);
    else
        throw "Number of likes input not valid";
    if(newNumberOfLikes < 0)
        throw("The number of likes should be a positive number");

    cout << "Enter link of the trailer" << endl;
    getline(cin, newTrailer);
    if(newTrailer.length() == 0)
        throw "Trailer input not valid";

    int updated = this->service->updateService(oldTitle, newTitle, newGenre, newYear, newNumberOfLikes, newTrailer);
    if(updated == 1)
        throw("The movie does not exist in the database");
    else if(updated == 0)
        cout <<"Movie updated successfully" << endl;

}

void UI::printAllAdmin() {
    Movie * movies = this->service->getAllService();
    int index;
    int numberOfElements = this->service->getSizeService();
    if(numberOfElements == 0)
        throw("There are no movies in the database");
    for(index = 0; index < numberOfElements; index ++)
        cout << index + 1 << ". " << movies[index].toString() << endl;
}

void UI::listFilteredUser(){
    string genreFilter;
    cout << "Enter the genre: " << endl;
    getline(cin, genreFilter);

    auto* validMovies = new Movie [this->service->getCapacityService()];
    int length = this->userService->getFiltered(validMovies, genreFilter);
    if(length == 0)
        throw "No movies corresponding";
    string option;
    bool done = false;
    int index = 0;
    while(!done)
    {
        if(length == 0)
            throw "No movies remained";
        if(index == length)
            index = 0;
        cout << validMovies[index].toString() << endl;
        cout << "Add to playlist? [Yes / No / Exit]" << endl;
        ShellExecuteA(NULL, NULL, "chrome.exe", validMovies[index].getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
        getline(cin, option);
        if (option == "Yes") {
            int found1 = 0;
            Movie movie1;
            movie1 = validMovies[index];
            for(int i = 0; i < length; i++)
                if(this->userService->getAllUsersService()[i] == movie1)
                    found1 = 1;
            if(found1 == 1) {
                cout << "The movie is already in the database" << endl;
            }
            else
            {
                Movie movie;
                movie = validMovies[index];
                this->userService->addUserService(movie);
            }
            index++;
        } else if (option == "No") {
            index++;
        } else if (option == "Exit")
            done = true;
    }
}

void UI::removeMovieUser()
{
    string titleRemoveMovie;
    cout << "What movie would you like to remove from the playlist?" << endl;
    getline(cin, titleRemoveMovie);

    int found = 0;
    int index = 0;
    int length = this->userService->getSizeService();
    for(int i = 0; i< length; i++)
        if(this->userService->getAllUsersService()[i].getTitle() == titleRemoveMovie) {
            found = 1;
            index = i;
        }

    if(found == 0)
        throw "The movie you want to remove does not exist in the playlist";
    else
    {
        int oldNumberOfLikes;
        string option;
        cout << "Would you like to rate the movie? [Yes / No]" << endl;
        getline(cin, option);
        if(option == "Yes")
        {
            this->service->findByTitleService(titleRemoveMovie);
            oldNumberOfLikes = this->service->getAllService()[index].getNumberOfLikes();
            this->service->getAllService()[index].setNumberOfLikes(oldNumberOfLikes + 1);
            this->userService->removeUserService(titleRemoveMovie);
        }
        else if(option == "No")
        {
            this->userService->removeUserService(titleRemoveMovie);
        }
        else
            cout << "Option not valid" << endl;
    }

}

void UI::listUserPlaylist()
{
    Movie * playlist = this->userService->getAllUsersService();
    int index;
    int numberOfElements = this->userService->getSizeService();
    if(numberOfElements == 0)
        throw "The list is empty!";
    for(index = 0; index < numberOfElements; index++)
        cout << index + 1 << ". " << playlist[index].toString() << endl;
}


void UI::adminMode()
{
    cout << " You are in admin mode" << endl;
    bool done = false;
    while(!done)
    {
        try
        {
            printMenuAdmin();
            string option;
            getline(cin, option);
            if(option == "0")
                done = true;
            else if(option == "1")
                this->printAllAdmin();
            else if(option == "2")
                this->addMovieAdmin();
            else if(option == "3")
                this->removeMovieAdmin();
            else if(option == "4")
                this->updateMovieAdmin();
            else
                cout << "Bad input! Try again" << endl;
        }
        catch(const char *msg)
        {
            cout << msg << endl;
        }
        catch (const exception &e)
        {
            cerr << e.what();
            cout << endl;
        }
    }

}

void UI::UserMode()
{
    cout << "You are in user mode" << endl;
    bool done = false;
    while(!done)
    {
        try
        {
            printMenuUser();
            string option;
            getline(cin, option);
            if(option == "0")
                done = true;
            else if(option == "1")
                this->listFilteredUser();
            else if(option == "2")
                this->removeMovieUser();
            else if(option == "3")
                this->listUserPlaylist();
        }
        catch(const char *msg)
        {
            cout << msg << endl;
        }
        catch (const exception &e)
        {
            cerr << e.what();
            cout << endl;
        }
    }
}


void UI::start(){
    cout << "Tinder Movie app!! Hello GABI" << endl;
    bool done = false;
    while(!done)
    {
        printMenuMode();
        string option;
        getline(cin, option);
        if(option == "1")
            adminMode();
        else if(option == "2")
            UserMode();
        else if(option == "0")
            done = true;
        else
            cout << "Bad input! Try again" << endl;

    }
}

UI::~UI() = default;