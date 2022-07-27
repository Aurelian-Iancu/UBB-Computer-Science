#include "userRepository.h"

UserRepository::UserRepository(DynamicVector <Movie> *playlist1) {
    this->playlist = playlist1;

}

Movie *UserRepository::getAllUsersRepo() {
    return this->playlist->getVector();
}

int UserRepository::getSize() {
    return this->playlist->getSize();
}

int UserRepository::getCapacity() {
    return this->playlist->getCapacity();
}

void UserRepository::addUserRepo(const Movie &movie) {
    this->playlist->addVector(movie);
}

void UserRepository::removeUserRepo(unsigned int index)
{
    this->playlist->removeVector(index);
}

int UserRepository::findByTitle(const std::string &title) {
    int searched_index = -1, index = 0, length;
    length = this->getSize();
    while(index < length && searched_index == -1)
    {
        Movie m = this->playlist->getVector()[index];
        std::string other_title = m.getTitle();
        if(other_title == title)
            searched_index = index;
        index ++;
    }
    return searched_index;
}

UserRepository::~UserRepository() = default;
