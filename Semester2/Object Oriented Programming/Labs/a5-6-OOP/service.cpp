#include "service.h"
#include "movie.h"
#include <exception>
#include "repository.h"


Service::Service(Repository *repo) {
    this->repository = repo;

}

Movie *Service::getAllService() {
    return this->repository->getRepo();
}

int Service::getSizeService() {
    return this->repository->getSize();
}

int Service::getCapacityService() {
    return this->repository->getCapacity();
}

int Service::addService(const std::string &title, const std::string &genre, int year, int numberOfLikes,const std::string &trailer) {
    int index;
    int length = this->repository->getSize();
    for(index = 0; index < length; index++)
    {
        std::string other_title = this->getAllService()[index].getTitle();
        if(other_title == title)
            return 1;
    }
    Movie m1 = Movie(title, genre, year, numberOfLikes, trailer);
    this->repository->addRepo(m1);
    return 0;
}

int Service::removeService(std::string title) {
    int delete_index = this->repository->findByTitle(title);
    if(delete_index == -1)
        return 1;
    else
    {
        this->repository->removeRepo(delete_index);
        return 0;
    }
}

int Service::findByTitleService(const std::string& title)
{
    int searchedIndex = repository->findByTitle(title);
    return searchedIndex;
}

int Service::updateService(const std::string oldName,const std::string newName, const std::string newGenre, int newYear, int newNumberOfLikes, const std::string newTrailer)
{
    int update_index = this->repository->findByTitle(oldName);
    if(update_index == -1)
        return 1;
    else
    {
        Movie newMovie;
        newMovie = Movie(newName, newGenre, newYear, newNumberOfLikes, newTrailer);
        this->repository->updateRepo(update_index, newMovie);
        return 0;
    }

}

Service::~Service() = default;






