#pragma once
#include "dynamicVector.h"

class Repository
{
private:
    DynamicVector<Movie>* database;
public:
    ///Constructor for the Repository class
    ///repoArray = The dynamic array in which we will store the movies
    explicit Repository(DynamicVector<Movie> *repoArray);

    ///Function used to initialise the repository
    void initialiseRepo();

    ///Getter for the repository
    Movie *getRepo();

    ///Getter for the capacity
    int getCapacity();

    ///Getter for the size
    int getSize();

    ///Function that returns the size of the repository
    unsigned int getSize() const { return this->database->getSize();}

    ///Function that adds a Movie to the repository
    void addRepo( Movie &m);

    ///Function that removes a Movie from the repository
    void removeRepo(int index);

    ///Function that updates a Movie from the repository
    void updateRepo(int index, Movie &newMovie);

    ///Function that finds a Movie by title in the repository
    int findByTitle(const std::string &title);

    ///Destructor
    ~Repository();



};
