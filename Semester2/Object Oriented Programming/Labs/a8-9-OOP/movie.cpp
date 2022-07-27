#include "movie.h"
#include <sstream>
#include <vector>
#include <iostream>


Movie::Movie(const std::string& title, const std::string& genre, const int year, const int numberOfLikes, const std::string& trailer)
        :title{ title }, genre{ genre }, year { year }, numberOfLikes {numberOfLikes}, trailer{ trailer }{}

bool Movie :: operator==(const Movie& movie)
{
    if(movie.title != this->title) return false;
/*    if(movie.genre != this->genre) return false;
    if(movie.year != this->year) return false;
    if(movie.numberOfLikes != this->numberOfLikes) return false;
    if(movie.trailer != this->trailer) return false;*/
    return true;
}

std::string Movie::toString() const
{
    auto strYear = std::to_string(this->year);
    auto strNumberOfLikes = std::to_string(this->numberOfLikes);
    return "Title: " + this->title + " | Genre: " + this->genre + " | Year: " + strYear + " | Number of likes: " + strNumberOfLikes
           + " | Trailer link: " + this->trailer;
}

std::vector<std::string> tokenize(const std::string& str, char delimiter) {
    std::vector<std::string> result;
    std::stringstream ss(str);
    std::string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}

std::istream &operator>>(std::istream &inputStream, Movie &movie) {
    std::string line;
    std::getline(inputStream, line);
    std::vector<std::string> tokens;
    if(line.empty())
        return inputStream;
    tokens = tokenize(line, ',');

    movie.title = tokens[0];
    movie.genre = tokens[1];
    movie.year = std::stoi(tokens[2]);
    movie.numberOfLikes = std::stoi(tokens[3]);
    movie.trailer = tokens[4];
    return inputStream;
}

std::ostream &operator<<(std::ostream &outputStream, const Movie &movieOutput) {
    outputStream << movieOutput.title << "," << movieOutput.genre << "," << movieOutput.year << "," << movieOutput.numberOfLikes
    << "," << movieOutput.trailer;
    return outputStream;
}








