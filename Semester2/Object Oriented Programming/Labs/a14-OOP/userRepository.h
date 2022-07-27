#pragma once
#include <vector>
#include "movie.h"

class UserRepository
{
protected:
    std::vector<Movie> playlist;
    std::string userFilename;
public:
    ///Constructor for the user repository
    explicit UserRepository(std::vector<Movie>& playlist1);

    UserRepository();

    ///Getter for the repository
    virtual std::vector<Movie>& getAllUsersRepo()=0;

    ///Getter for the size
    virtual unsigned int getSize()=0;

    ///Getter for the capacity
    virtual unsigned int getCapacity()=0;

    ///Function that adds a movie to the repository
    virtual void addUserRepo(const Movie& movie)=0;

    ///Destructor for the user repository
    ~UserRepository();

    ///Function that removes a movie from a certain index of the repository
    virtual void removeUserRepo(unsigned int index)=0;

    ///Function used to find a Movie by its title in the repository
    virtual int findByTitle(const std::string &title)=0;

    virtual void writeToFile()=0;

    virtual std::string& getFilename()=0;
};

class UserException: public std::exception {
private:
    std::string message;
public:
    explicit UserException(std::string& _message);

    const char *what() const noexcept override;
};
