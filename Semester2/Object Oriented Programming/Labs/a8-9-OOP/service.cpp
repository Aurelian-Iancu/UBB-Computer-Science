#include "service.h"
#include "movie.h"
#include <algorithm>
#include <exception>


Service::Service(Repository& repo) : repository(repo){}

std::vector<Movie>& Service::getAllService() {
    return this->repository.getRepo();
}

unsigned int Service::getSizeService() {
    return this->repository.getSize();
}

void Service::addService(const std::string &title, const std::string &genre, int year, int numberOfLikes,const std::string &trailer) {
        Movie movie = Movie(title, genre, year, numberOfLikes, trailer);
        this->repository.addRepo(movie);
}

void Service::removeService(std::string title) {
    int delete_index = this->repository.findByTitle(title);
    this->repository.removeRepo(delete_index);
}

int Service::findByTitleService(const std::string& title)
{
    int searchedIndex = repository.findByTitle(title);
    return searchedIndex;
}

void Service::updateService(const std::string oldName,const std::string newName, const std::string newGenre, int newYear, int newNumberOfLikes, const std::string newTrailer)
{
    int update_index = this->repository.findByTitle(oldName);
    Movie movie = Movie(newName, newGenre, newYear, newNumberOfLikes, newTrailer);
    this->repository.updateRepo(update_index, movie);
}

void Service::writeToFileService()
{
    this->repository.writeToFileRepo();
}

Service::~Service() = default;






