#include "movie.h"
#include <iomanip>

using std::ostream;

Movie::Movie(const std::string& title, const std::string& genre, const int year, const int numberOfLikes, const std::string& trailer)
    :title{ title }, genre{ genre }, year { year }, numberOfLikes {numberOfLikes}, trailer{ trailer }{}

bool Movie :: operator==(const Movie& movie)
{
    if(movie.title != this->title) return false;
    if(movie.genre != this->genre) return false;
    if(movie.year != this->year) return false;
    if(movie.numberOfLikes != this->numberOfLikes) return false;
    if(movie.trailer != this->trailer) return false;
    return true;
}

std::string Movie::toString() const
{
    auto strYear = std::to_string(this->year);
    auto strNumberOfLikes = std::to_string(this->numberOfLikes);
    return "Title: " + this->title + " | Genre: " + this->genre + " | Year: " + strYear + " | Number of likes: " + strNumberOfLikes
            + " | Trailer link: " + this->trailer;
}

