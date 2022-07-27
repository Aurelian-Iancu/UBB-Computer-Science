#include "userService.h"
#include "HTMLrepository.h"
#include "CSVrepository.h"
#include <algorithm>

UserService::UserService(Repository& repository1, UserRepository* userRepository1): repository(repository1)
{
    this->userRepository = userRepository1;
}

std::vector<Movie> UserService::getAllUsersService() {
    return this->userRepository->getAllUsersRepo();
}

unsigned int UserService::getSizeService() {
    return this->userRepository->getSize();
}

void UserService::addUserService(Movie &movie) {
    this->userRepository->addUserRepo(movie);
}

void UserService::removeUserService(std::string &title)
{
    int index = this->userRepository->findByTitle(title);
    this->userRepository->removeUserRepo(index);
}

int UserService::getFiltered(std::vector<Movie>& validMovies, std::string& filter_string) {
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
    return validMovies.size();
}

std::string &UserService::getFileService() {
    return this->userRepository->getFilename();
}

void UserService::repositoryType(const std::string &fileType) {
    if (fileType == "csv") {
        std::vector<Movie> userVector;
        std::string userFile = R"(C:\Users\Aurelian\Documents\GitHub\OOP\a8-9-913-Iancu-Gheorghe-Aurelian\Playlist.csv)";
        auto *repo = new CSVRepo{userVector, userFile};
        this->userRepository = repo;
    } else if (fileType == "html") {
        std::vector<Movie> userVector;
        std::string userFile = R"(C:\Users\Aurelian\Documents\GitHub\OOP\a8-9-913-Iancu-Gheorghe-Aurelian\Playlist.html)";
        auto *repo = new HTMLRepo{userVector, userFile};
        this->userRepository = repo;
    } else {
        std::string error;
        error += std::string("The filename is invalid!");
        if (!error.empty())
            throw UserException(error);
    }
}

UserService::UserService(Repository &repository1): repository{repository1}{}

UserService::~UserService() = default;



