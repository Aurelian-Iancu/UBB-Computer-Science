
#include "userService.h"

UserService::UserService(Repository *repository1, UserRepository *userRepository1) {
    this->repository = repository1;
    this->userRepository = userRepository1;

}

Movie *UserService::getAllUsersService() {
    return this->userRepository->getAllUsersRepo();
}

int UserService::getSizeService() {
    return this->userRepository->getSize();
}

int UserService::getCapacityService() {
    return this->userRepository->getCapacity();
}

void UserService::addUserService(Movie &movie) {
    this->userRepository->addUserRepo(movie);
/*    std::string title = movie.getTitle();
    int delete_index = this->repository->findByTitle(title);
    this->repository->removeRepo(delete_index);*/
}

void UserService::removeUserService(std::string &title)
{
    int index = this->userRepository->findByTitle(title);
    //Movie movie;
    //movie = this->userRepository->getAllUsersRepo()[index];
    this->userRepository->removeUserRepo(index);
    //this->repository->addRepo(movie);
}

int UserService::getFiltered(Movie *validMovies, std::string filter_string) {
    int index;
    int counter = 0;
    int length = this->repository->getSize();
    if(filter_string[0] == '\0')
    {
        for(index = 0; index < length; index++)
        {
            Movie movie;
            movie = this->repository->getRepo()[index];
            validMovies[counter] = movie;
            counter++;
        }
    }
    else
    {
        for(index = 0; index < length; index++) {
            Movie movie;
            movie = this->repository->getRepo()[index];
            if(filter_string == movie.getGenre())
            {
                validMovies[counter] = movie;
                counter++;
            }
        }

    }
    return counter;
}

UserService::~UserService() = default;

