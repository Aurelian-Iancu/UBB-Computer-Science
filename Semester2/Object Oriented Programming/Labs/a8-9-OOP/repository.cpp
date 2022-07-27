#include "repository.h"
#include <string>
#include <algorithm>
#include <fstream>

RepositoryException::RepositoryException(std::string &_message): message(_message) {}

const char* RepositoryException::what() const noexcept {
    return message.c_str();
}

Repository::Repository(std::vector<Movie>& repo_vector, std::string& movieFile) {
    this->database = repo_vector;
    this->moviesFile = movieFile;
}

void Repository::loadMoviesFromFile() {
    if(!this->moviesFile.empty())
    {
        Movie movieFromFile;
        std::ifstream fin(this->moviesFile);
        while(fin >> movieFromFile)
        {
            if(std::find(this->database.begin(), this->database.end(), movieFromFile) == this->database.end())
                this->database.push_back(movieFromFile);
        }
        fin.close();
    }
}

void Repository::writeMoviesToFile() {
    if (!this->moviesFile.empty()) {
        std::ofstream fout(this->moviesFile);
        for (const Movie &movie: this->database) {
            fout << movie << "\n";
        }
        fout.close();
    }
}

void Repository::initialiseRepo()
{
    this->loadMoviesFromFile();
}

std::vector<Movie>& Repository::getRepo()
{
    if(this->database.empty())
    {
        std::string errors;
        errors += std::string("The database is empty!");
        if(!errors.empty())
            throw RepositoryException(errors);
    }
    return this->database;
}

unsigned int Repository::getSize()
{
    if(this->database.empty())
    {
        std::string errors;
        errors += std::string("The database is empty!");
        if(!errors.empty())
            throw RepositoryException(errors);
    }
    return this->database.size();
}

void Repository::addRepo( Movie &m) {
    int existing = this->findByTitle(m.getTitle());
    if(existing != -1)
    {
        std::string errors;
        errors += std::string("The movie is already in the database!");
        if(!errors.empty())
            throw RepositoryException(errors);
    }
    this -> database.push_back(m);
    this -> writeMoviesToFile();
}

int Repository::findByTitle(const std::string &title) {
    int searchedIndex = -1;
    std::vector<Movie>::iterator it;
    it = std::find_if(this->database.begin(), this->database.end(), [&title](Movie& movie) {return movie.getTitle() == title;});
    if(it != this->database.end())
        searchedIndex = it - this->database.begin();
    return searchedIndex;
}

void Repository::removeRepo(int index) {
    if(index == -1)
    {
        std::string errors;
        errors += std::string("The movie does not exist!");
        if(!errors.empty())
            throw RepositoryException(errors);
    }
    this-> database.erase(this->database.begin() + index);
    this->writeMoviesToFile();
}

void Repository::updateRepo(int index, Movie &newMovie)
{
    if(index == -1)
    {
        std::string errors;
        errors += std::string("The movie does not exist!");
        if(!errors.empty())
            throw RepositoryException(errors);
    }
    this->database[index] = newMovie;
    this->writeMoviesToFile();

}

void Repository::writeToFileRepo()
{
    this->writeMoviesToFile();
}

Repository::~Repository() = default;

