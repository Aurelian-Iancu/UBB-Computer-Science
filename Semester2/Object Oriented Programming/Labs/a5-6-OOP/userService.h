#pragma once
#include <repository.h>
#include <userRepository.h>

class UserService{
private:
    Repository* repository;
    UserRepository* userRepository;
public:
    ///Constructor for the user service
    UserService(Repository* repository1, UserRepository* userRepository1);

    ///Getter for the repository in service
    Movie * getAllUsersService();

    ///Getter for the size in service
    int getSizeService();

    ///Getter for the capacity in service
    int getCapacityService();

    ///This function adds a movie to the repository in service
    void addUserService(Movie &movie);

    ///This function returns the number of movies that are of a certain genre(filter_string)
    int getFiltered(Movie* validMovies, std::string filter_string);

    ///Destructor
    ~UserService();

    ///This function removes a movie from the repository that have a certain title
    void removeUserService(std::string &title);
};