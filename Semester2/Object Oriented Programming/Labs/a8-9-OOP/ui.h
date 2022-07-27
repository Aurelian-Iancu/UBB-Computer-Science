#pragma once
#include "service.h"
#include "userService.h"
#include "validators.h"

class UI{
private:
    Service& service;
    UserService& userService;
    MovieValidator& validator;
public:
    ///Constructor for the UI
    explicit UI(Service& service, UserService& userService, MovieValidator& validator1);

    ///Function used to print the menu for the modes
    void printMenuMode();

    ///Function used to print the menu for the admin mode
    static void printMenuAdmin();

    ///Function used to add a Movie in admin mode
    void addMovieAdmin();

    ///Function used to print the repository in admin mode
    void printAllAdmin();

    ///Function used to start the application
    void start();

    ///Function used to remove a Movie in admin mode
    void removeMovieAdmin();

    ///Function used to update a Movie in admin mode
    void updateMovieAdmin();

    ///Function that prints the menu of the user
    void printMenuUser();

    ///Here we basically call what we can do in user mode and we catch the exceptions
    void UserMode();

    ///Here we basically call what we can do in the admin mode and we catch the exceptions
    void adminMode();

    ///Destructor of the UI
    ~UI();

    ///Function that lists the list of users filtered by a the genre
    void listFilteredUser();

    ///Function that lists the movie playlist
    void listUserPlaylist();

    ///Function that removes a movie from the playlist
    void removeMovieUser();

    void openFile();
};
