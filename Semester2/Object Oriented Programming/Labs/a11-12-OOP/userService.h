#pragma once
#include "repository.h"
#include "userRepository.h"

class UserService{
private:
    Repository& repository;
    UserRepository* userRepository;
public:
    ///Constructor for the user service
    UserService(Repository& repository1, UserRepository& userRepository1);

    explicit UserService(Repository& repository1);

    ///Getter for the repository in service
    std::vector<Movie> getAllUsersService();

    ///Getter for the size in service
    unsigned int getSizeService();

    ///This function adds a movie to the repository in service
    void addUserService(Movie &movie);

    ///This function returns the number of movies that are of a certain genre(filter_string)
    int getFiltered(std::vector<Movie>& validMovies, std::string& filter_string);

    std::string& getFileService();

    void repositoryType(const std::string& fileType);

    ///Destructor
    ~UserService();

    ///This function removes a movie from the repository that have a certain title
    void removeUserService(std::string &title);
};
