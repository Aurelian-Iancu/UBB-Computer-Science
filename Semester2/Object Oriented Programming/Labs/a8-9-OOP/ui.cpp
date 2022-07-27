#include "ui.h"
#include <windows.h>
#include <shellapi.h>
#include <iostream>
#include <vector>
using namespace std;

UI::UI(Service& service, UserService& userService, MovieValidator& validator1): service(service), userService(userService), validator(validator1)
{
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
    cout<<"4. See the playlist file.\n";
    cout << "0. To exit the user mode\n";
}

void UI::addMovieAdmin(){
    cout << "Add a new movie" << endl;
    string title, genre, yearS, numberOfLikesS, trailer;
    int year, numberOfLikes;

    while(true)
    {
        try{
        cout << "Enter the title" << endl;
        getline(cin , title);
        this->validator.validateTitle(title);
        break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter the genre" << endl;
            getline(cin, genre);
            this->validator.validateGenre(genre);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter the year of release" << endl;
            getline(cin, yearS);
            this->validator.validateYearString(yearS);
            year = stoi(yearS);
            this->validator.validateYear(year);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter the number of likes" << endl;
            getline(cin, numberOfLikesS);
            this->validator.validateLikesString(numberOfLikesS);
            numberOfLikes = stoi(numberOfLikesS);
            this->validator.validateYearLikes(numberOfLikes);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter link of the trailer" << endl;
            getline(cin, trailer);
            this->validator.validateTrailer(trailer);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }
    this->service.addService(title, genre, year, numberOfLikes, trailer);
    cout << "Movie successfully added!" << endl;

}

void UI::removeMovieAdmin(){
    cout << "Delete a movie" << endl;
    string title;

    while(true)
    {
        try{
            cout << "Enter the title" << endl;
            getline(cin , title);
            this->validator.validateTitle(title);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    this->service.removeService(title);
    cout << "Movie successfully removed!" << endl;

}

void UI::updateMovieAdmin() {
    cout << "Update a movie" << endl;
    string oldTitle, newTitle, newGenre, newYearS, newNumberOfLikesS, newTrailer;
    int newYear, newNumberOfLikes;

    while(true)
    {
        try{
            cout << "Enter the old title" << endl;
            getline(cin , oldTitle);
            this->validator.validateTitle(oldTitle);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter the new title" << endl;
            getline(cin , newTitle);
            this->validator.validateTitle(newTitle);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter the genre" << endl;
            getline(cin, newGenre);
            this->validator.validateGenre(newGenre);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter the year of release" << endl;
            getline(cin, newYearS);
            this->validator.validateYearString(newYearS);
            newYear = stoi(newYearS);
            this->validator.validateYear(newYear);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter the number of likes" << endl;
            getline(cin, newNumberOfLikesS);
            this->validator.validateLikesString(newNumberOfLikesS);
            newNumberOfLikes = stoi(newNumberOfLikesS);
            this->validator.validateYearLikes(newNumberOfLikes);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    while(true)
    {
        try{
            cout << "Enter link of the trailer" << endl;
            getline(cin, newTrailer);
            this->validator.validateTrailer(newTrailer);
            break;
        }
        catch(ValidationException& exception)
        {
            cout << exception.what() << endl;
        }
    }

    this->service.updateService(oldTitle, newTitle, newGenre, newYear, newNumberOfLikes, newTrailer);
    cout << "Movie updated successfully!" << endl;

}

void UI::printAllAdmin() {
    std::vector<Movie> movies;
    movies = this->service.getAllService();
    int index = 0;
    for(const Movie& movie: movies)
    {
        cout << index + 1 << ". " << movie.toString() << endl;
        index++;
    }
}

void UI::listFilteredUser(){
    string genreFilter;
    cout << "Enter the genre: " << endl;
    getline(cin, genreFilter);

    std::vector<Movie> validMovies;
    validMovies.reserve(this->service.getSizeService());
    std::vector<Movie> playlist;
    playlist.reserve(this->userService.getSizeService());
    playlist = this->userService.getAllUsersService();

    int length = this->userService.getFiltered(validMovies, genreFilter);
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
            Movie movie;
            movie = validMovies[index];
            for(Movie& m: playlist)
                if(movie == m)
                    found1 = 1;
            if(found1 == 1)
            {
                cout << "The movie is already in the database" << endl;
            }
            else
            {
                this->userService.addUserService(movie);
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

    std::vector<Movie> playlist;
    playlist.reserve(this->userService.getSizeService());
    playlist = this->userService.getAllUsersService();

    int found = 0;
    int index;
    for(Movie& m: playlist)
        if(m.getTitle() == titleRemoveMovie)
            found = 1;
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
            index = this->service.findByTitleService(titleRemoveMovie);
            oldNumberOfLikes = this->service.getAllService()[index].getNumberOfLikes();
            this->service.getAllService()[index].setNumberOfLikes(oldNumberOfLikes + 1);
            this->service.writeToFileService();
            this->userService.removeUserService(titleRemoveMovie);
        }
        else if(option == "No")
        {
            this->userService.removeUserService(titleRemoveMovie);
        }
        else
            cout << "Option not valid" << endl;
    }

}

void UI::listUserPlaylist()
{
    std::vector<Movie> playlist;
    playlist = this->userService.getAllUsersService();
    int index = 0;
    unsigned int numberOfElements = this->userService.getSizeService();
    if(numberOfElements == 0)
        throw "The playlist is empty!";
    for(const Movie& movie: playlist) {
        cout << index + 1 << ". " << movie.toString() << endl;
        index++;
    }
}

void UI::openFile()
    {
        std::string link = std::string("start ").append(this->userService.getFileService());
        system(link.c_str());
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
            else if(option == "4")
                this->openFile();
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
    int usermode = 0;
    bool done = false;
    while(!done)
    {
        printMenuMode();
        string option;
        getline(cin, option);
        if(option == "1")
            adminMode();
        else if(option == "2")
        {
            if(usermode == 0)
            {
                std::cout<<"Enter the type of the file in which you want to save the adoption list(csv or html):"<<std::endl;
                std::string fileType;
                while (true) {
                    try {
                        getline(std::cin, fileType);
                        this->userService.repositoryType(fileType);
                        break;
                    }catch (UserException& ex) {
                        std::cout<<ex.what()<<std::endl;
                    }
                }
                usermode = 1;
            }
            UserMode();
        }
        else if(option == "0")
            done = true;
        else
            cout << "Bad input! Try again" << endl;

    }
}

UI::~UI() = default;

