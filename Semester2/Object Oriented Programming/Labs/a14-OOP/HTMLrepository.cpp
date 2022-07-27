#include <fstream>
#include <algorithm>
#include "HTMLrepository.h"

HTMLRepo::HTMLRepo(const std::vector<Movie> &playlist, const std::string &userFilename) {
    this->playlist = playlist;
    this->userFilename = userFilename;
}

std::vector<Movie>& HTMLRepo::getAllUsersRepo() {
    return this->playlist;
}

unsigned int HTMLRepo::getSize() {
    return this->playlist.size();
}

unsigned int HTMLRepo::getCapacity() {
    return this->playlist.capacity();
}

void HTMLRepo::addUserRepo(const Movie &movie) {
    int existing = this->findByTitle(movie.getTitle());
    if(existing != -1)
    {
        std::string errors;
        errors += std::string("The movie is already in the playlist!");
        if(!errors.empty())
            throw UserException(errors);
    }
    this->playlist.push_back(movie);
    this->writeToFile();
}

void HTMLRepo::removeUserRepo(unsigned int index) {
    this->playlist.erase(this->playlist.begin() + index);
    this->writeToFile();
}

int HTMLRepo::findByTitle(const std::string &title) {
    int searchedIndex = -1;
    std::vector<Movie>::iterator it;
    it = std::find_if(this->playlist.begin(), this->playlist.end(), [&title](Movie& movie) {return movie.getTitle() == title;});
    if(it != this->playlist.end())
        searchedIndex = it - this->playlist.begin();
    return searchedIndex;
}

void HTMLRepo::writeToFile() {
    std::ofstream fout(this->userFilename);
    fout << "<!DOCTYPE html>\n<html><head><title>Playlist</title></head><body>\n";
    fout << "<table border=\"1\">\n";
    fout << "<tr><td>Title</td><td>Genre</td><td>Year of release</td><td>Number of likes</td><td>Trailer</td></tr>\n";
    for(const Movie& movie: this->playlist)
    {
        fout << "<tr><td>" << movie.getTitle() << "</td>"
             << "<td>" << movie.getGenre() << "</td>"
             << "<td>" << std::to_string(movie.getYear()) << "</td>"
             << "<td>" << std::to_string(movie.getNumberOfLikes()) << "</td>"
             << "<td><a href=\"" << movie.getTrailer() << "\">" << movie.getTrailer() << "</a></td>" << '\n';
    }
    fout << "</table></body></html>";
    fout.close();
}

std::string &HTMLRepo::getFilename() {
    return this->userFilename;
}

HTMLRepo::~HTMLRepo() = default;


