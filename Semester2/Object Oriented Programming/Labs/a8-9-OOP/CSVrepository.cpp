#include <algorithm>
#include <fstream>
#include "CSVrepository.h"

CSVRepo::CSVRepo(const std::vector<Movie> &playlist, const std::string &userFilename) {
    this->playlist = playlist;
    this->userFilename = userFilename;
}

std::vector<Movie> &CSVRepo::getAllUsersRepo() {
    return this->playlist;
}

unsigned int CSVRepo::getSize() {
    return this->playlist.size();
}

unsigned int CSVRepo::getCapacity() {
    return this->playlist.capacity();
}

void CSVRepo::addUserRepo(const Movie &movie) {
    this->playlist.push_back(movie);
    this->writeToFile();
}

void CSVRepo::removeUserRepo(unsigned int index) {
    this->playlist.erase(this->playlist.begin() + index);
    this->writeToFile();
}

int CSVRepo::findByTitle(const std::string &title) {
    int searchedIndex = -1;
    std::vector<Movie>::iterator it;
    it = std::find_if(this->playlist.begin(), this->playlist.end(), [&title](Movie& movie) {return movie.getTitle() == title;});
    if(it != this->playlist.end())
        searchedIndex = it - this->playlist.begin();
    return searchedIndex;
}

void CSVRepo::writeToFile() {
    std::ofstream fout(this->userFilename);
    if (!this->playlist.empty()) {
        for (const Movie& movie: this->playlist) {
            fout<<movie<<"\n";
        }
    }
    fout.close();
}

std::string &CSVRepo::getFilename() {
    return this->userFilename;
}

CSVRepo::~CSVRepo() = default;

