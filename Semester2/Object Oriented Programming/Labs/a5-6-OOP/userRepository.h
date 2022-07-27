#pragma once
#include "dynamicVector.h"

class UserRepository
{
private:
    DynamicVector<Movie>* playlist;
public:
    ///Constructor for the user repository
    explicit UserRepository(DynamicVector<Movie> * playlist1);

    ///Getter for the repository
    Movie * getAllUsersRepo();

    ///Getter for the size
    int getSize();

    ///Getter for the capacity
    int getCapacity();

    ///Function that adds a movie to the repository
    void addUserRepo(const Movie& movie);

    ///Destructor for the user repository
    ~UserRepository();

    ///Function that removes a movie from a certain index of the repository
    void removeUserRepo(unsigned int index);

    ///Function used to find a Movie by its title in the repository
    int findByTitle(const std::string &title);
};
