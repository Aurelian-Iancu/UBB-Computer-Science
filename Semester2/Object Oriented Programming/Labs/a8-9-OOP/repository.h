#pragma once
#include "vector"
#include "movie.h"

class Repository
{
private:
    std::vector<Movie> database;
    std::string moviesFile;

public:
    void loadMoviesFromFile();

    void writeMoviesToFile();
    ///Constructor for the Repository class
    ///repoArray = The dynamic array in which we will store the movies
    explicit Repository(std::vector<Movie>& repo_vector, std::string& movieFile);

    ///Function used to initialise the repository
    void initialiseRepo();

    ///Getter for the repository
    std::vector<Movie>& getRepo();

    ///Getter for the size
    unsigned int getSize();

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

    void writeToFileRepo();
};

class RepositoryException: public std::exception{
private:
    std::string message;

public:
    explicit RepositoryException(std::string& _message);

    const char* what() const noexcept override;

};