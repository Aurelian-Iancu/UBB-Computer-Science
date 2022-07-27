#pragma once

#include <string>
#include <vector>


class Movie
{
private:
    std::string title;
    std::string genre;
    int year;
    int numberOfLikes;
    std::string trailer;

public:
    ///Constructor for the Movie class;
    Movie() : title{"" }, genre{"" }, year{ 0 }, numberOfLikes{0 }, trailer{"" }{}

    ///Function used to create a Movie object
    Movie(const std::string& title, const std::string& genre, int year, int numberOfLikes, const std::string& trailer);

    ///Function used to get the title of a Movie
    std::string getTitle() const { return this->title; }

    /// Function used to get the genre of a Movie
    std::string getGenre() const { return this->genre; }

    ///Function used to get the year of a Movie
    int getYear() const { return this->year; }

    ///Function used to get the number of likes of a Movie
    int getNumberOfLikes() const { return this->numberOfLikes; }

    ///Function used to get the trailer of the movie
    std::string getTrailer() const { return this->trailer; }

    ///Setter for the number of likes
    void setNumberOfLikes(int newNumberOfLikes) { this->numberOfLikes = newNumberOfLikes ;}

    ///Function to overwrite the == operator(Now we can see if 2 objects of type Movie are equal)
    bool operator==(const Movie& movie) ;

    ///Function that returns the way we want to print a Movie
    std::string toString() const;

    friend std::istream& operator>>(std::istream& inputStream, Movie& movie);

    friend std::ostream & operator<<(std::ostream& outputStream, const Movie& movieOutput);

    };
