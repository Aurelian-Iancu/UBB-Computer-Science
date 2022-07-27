#pragma once
#include "repository.h"
#include <string>
#include <memory>
#include "undoRedo.h"

class Service{
    Repository& repository;
    std::vector<std::shared_ptr<UndoRedoAction>> undoAdmin;
    std::vector<std::shared_ptr<UndoRedoAction>> redoAdmin;
public:
    ///Service constructor
    explicit Service(Repository& repo);

    ///Getter for the repository in service
    std::vector<Movie>& getAllService();

    ///Getter for the size in service
    unsigned int getSizeService();

    ///Function that adds a Movie in the service
    void addService(const std::string &title, const std::string &genre, int year, int numberOfLikes,const std::string &trailer);

    ///Function that removes a Movie with a certain title from the repository
    void removeService(std::string title);

    ///Function that updates a Movie
    void updateService(const std::string oldName,const std::string newName, const std::string newGenre,
                       int newYear, int newNumberOfLikes, const std::string newTrailer);

    ///Destructor for the service class
    ~Service();

    int findByTitleService(const std::string &title);

    void writeToFileService();

    void getFiltered(std::vector<Movie>& validMovies, std::string& filter_string);

    std::vector<std::string> getAllOfGenre();

    int numberOfMoviesPerGenre(const std::string& genre);

    void undoLastAction();
    void redoLastAction();
    void clearUndoRedo();
};