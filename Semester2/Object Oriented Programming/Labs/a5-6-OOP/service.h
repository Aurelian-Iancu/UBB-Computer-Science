#pragma once
#include "repository.h"
#include <string>
#include <vector>
#include "comparator.h"

class Service{
    Repository *repository;
public:
    ///Service constructor
    explicit Service(Repository *repo);

    ///Getter for the repository in service
    Movie * getAllService();

    ///Getter for the size in service
    int getSizeService();

    ///Getter for the capacity in service
    int getCapacityService();

    ///Function that adds a Movie in the service
    int addService(const std::string &title, const std::string &genre, int year, int numberOfLikes,const std::string &trailer);

    ///Function that removes a Movie with a certain title from the repository
    int removeService(std::string title);

    ///Function that updates a Movie
    int updateService(const std::string oldName,const std::string newName, const std::string newGenre,
                               int newYear, int newNumberOfLikes, const std::string newTrailer);

    ///Destructor for the service class
    ~Service();

    int findByTitleService(const std::string &title);
};

template <typename TElem>
void sortElements(std::vector<TElem>& v, Comparator<TElem>* c) {

    bool sorted = true;

    do
    {
        sorted = true;

        for (int i = 0; i < v.size() - 1; i++)
        {
            if (!c->compare(v[i], v[i + 1]))
            {
                std::swap(v[i], v[i + 1]);
                sorted = false;
            }
        }
    } while (!sorted);

}