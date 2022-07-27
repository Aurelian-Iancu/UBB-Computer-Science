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
    std::shared_ptr<UndoRedoAction> action = std::make_shared<UndoRedoAdd>(movie, this->repository);
    //auto idk = UndoRedoAdd(movie, this->repository);
    this->undoAdmin.push_back(action);
}

void Service::removeService(std::string title) {
    int delete_index = this->repository.findByTitle(title);
    Movie movie = this->repository.getRepo()[delete_index];
    this->repository.removeRepo(delete_index);
    std::shared_ptr<UndoRedoAction> action = std::make_shared<UndoRedoRemove>(movie, this->repository);
    this->undoAdmin.push_back(action);
}

int Service::findByTitleService(const std::string& title)
{
    int searchedIndex = repository.findByTitle(title);
    return searchedIndex;
}

void Service::updateService(const std::string oldName,const std::string newName, const std::string newGenre, int newYear, int newNumberOfLikes, const std::string newTrailer)
{
    int update_index = this->repository.findByTitle(oldName);
    Movie oldMovie = this->repository.getRepo()[update_index];
    Movie newMovie = Movie(newName, newGenre, newYear, newNumberOfLikes, newTrailer);
    this->repository.updateRepo(update_index, newMovie);
    std::shared_ptr<UndoRedoAction> action = std::make_shared<UndoRedoUpdate>(oldMovie, newMovie, this->repository);
    this->undoAdmin.push_back(action);
}

void Service::writeToFileService()
{
    this->repository.writeToFileRepo();
}

void Service::getFiltered(std::vector<Movie>& validMovies, std::string& filter_string) {
    std::vector<Movie> result;
    result.resize(this->repository.getSize());
    result = this->repository.getRepo();
    if(filter_string[0] == '\0')
    {
        std::copy_if(result.begin(), result.end(), std::back_inserter(validMovies),[](Movie& movie) { return true; });
    }
    else
    {
        std::copy_if(result.begin(), result.end(), std::back_inserter(validMovies),[&filter_string](Movie& movie) { return movie.getGenre() == filter_string; });
    }
}

std::vector<std::string> Service::getAllOfGenre() {
    std::vector<std::string> movies;
    std::vector<Movie> data;
    data = this->repository.getRepo();
    for (const Movie& movie: data) {
        if (std::find(movies.begin(), movies.end(), movie.getGenre()) == movies.end())
            movies.push_back(movie.getGenre());
    }
    return movies;
}

int Service::numberOfMoviesPerGenre(const std::string& genre) {
    int count = 0;
    std::vector<Movie> data;
    data = this->repository.getRepo();
    for (const Movie& movie: data) {
        if (movie.getGenre() == genre) {
            count += 1;
        }
    }
    return count;
}

Service::~Service() = default;


void Service::undoLastAction() {
    if(this->undoAdmin.empty())
    {
        std::string error;
        error += std::string("No more undoes left!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->undoAdmin.back()->undo();
    this->redoAdmin.push_back(this->undoAdmin.back());
    this->undoAdmin.pop_back();
}

void Service::redoLastAction() {
    if (this->redoAdmin.empty()){
        std::string error;
        error += std::string("No more redoes left!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->redoAdmin.back()->redo();
    this->undoAdmin.push_back(this->redoAdmin.back());
    this->redoAdmin.pop_back();
}

void Service::clearUndoRedo() {
    this->undoAdmin.clear();
    this->redoAdmin.clear();
}
