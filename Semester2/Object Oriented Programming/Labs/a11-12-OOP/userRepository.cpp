#include "userRepository.h"
#include <algorithm>


UserException::UserException(std::string &_message): message(_message) {}

const char* UserException::what() const noexcept {
    return message.c_str();
}


UserRepository::UserRepository() = default;

UserRepository::UserRepository(std::vector<Movie>& playlist1) {
    this->playlist = playlist1;
}

std::vector<Movie>& UserRepository::getAllUsersRepo() {
    return this->playlist;
}

UserRepository::~UserRepository() = default;

