#include "repository.h"
#include <stdexcept>
#include <string>



Repository::Repository(DynamicVector<Movie> *repoArray) {
    this->database = repoArray;
}

void Repository::initialiseRepo()
{
    Movie m1 = Movie("The Shawshank Redemption", "Drama", 1994, 2563415,
                     "https://www.imdb.com/video/vi3877612057?playlistId=tt0111161&ref_=tt_ov_vi");
    Movie m2 = Movie("The Godfather", "Drama, Crime", 1972, 1764309,
                     "https://www.imdb.com/video/vi1348706585?playlistId=tt0068646&ref_=tt_ov_vi");
    Movie m3 = Movie("The Dark knight", "Action, Crime, Drama", 2008, 2525427,
                     "https://www.imdb.com/video/vi324468761?playlistId=tt0468569&ref_=tt_ov_vi");
    Movie m4 = Movie("The Godfather: part II", "Drama, Crime", 1974, 1221431,
                     "https://www.imdb.com/video/vi696162841?playlistId=tt0071562&ref_=tt_pr_ov_vi");
    Movie m5 = Movie("12 Angry Men", "Crime, Drama", 1957, 757166,
                     "https://www.imdb.com/video/vi3452609817?playlistId=tt0050083&ref_=tt_pr_ov_vi");
    Movie m6 = Movie("Schindler's List", "Biography, Drama, History", 1993, 1306699,
                     "https://www.imdb.com/video/vi1158527769?playlistId=tt0108052&ref_=tt_pr_ov_vi");
    Movie m7 = Movie("The Lord of the Rings: The Return of the King", "Action, Adventure, Drama", 2003,
                     1764464, "https://www.imdb.com/video/vi718127897?playlistId=tt0167260&ref_=tt_ov_vi");
    Movie m8 = Movie("Pulp fiction", "Crime, Drama", 1994, 1968553,
                     "https://www.imdb.com/video/vi2620371481?playlistId=tt0110912&ref_=tt_pr_ov_vi");
    Movie m9 = Movie("The Lord of the Rings: The Fellowship of the Ring", "Action, Adventure, Drama", 2001,
                     1786262, "https://www.imdb.com/video/vi684573465?playlistId=tt0120737&ref_=tt_pr_ov_vi");
    Movie m10 = Movie("The good, the bad and the ugly", "Adventure, Western", 1966, 737806,
                      "https://www.imdb.com/video/vi3416964889?playlistId=tt0060196&ref_=tt_pr_ov_vi");
    this->database->addVector(m1);
    this->database->addVector(m2);
    this->database->addVector(m3);
    this->database->addVector(m4);
    this->database->addVector(m5);
    this->database->addVector(m6);
    this->database->addVector(m7);
    this->database->addVector(m8);
    this->database->addVector(m9);
    this->database->addVector(m10);


}

Movie* Repository::getRepo()
{
    return this->database->getVector();
}

int Repository::getCapacity()
{
    return this->database->getCapacity();
}

int Repository::getSize()
{
    return this->database->getSize();
}

void Repository::addRepo( Movie &m) {
    this -> database->addVector(m);
}

int Repository::findByTitle(const std::string &title) {
    int searched_index = -1, index = 0, length;
    length = this->getSize();
    while(index < length && searched_index == -1)
    {
        Movie m = this->database->getVector()[index];
        std::string other_title = m.getTitle();
        if(other_title == title)
            searched_index = index;
        index ++;
    }
    return searched_index;
}

void Repository::removeRepo(int index) {
    this-> database->removeVector(index);
}

void Repository::updateRepo(int index, Movie &newMovie)
{
    this->database->updateVector(index, newMovie);

}

Repository::~Repository() = default;




