
#include "movie.h"
#include "repository.h"
#include "service.h"
#include "tests.h"
#include "userRepository.h"
#include "userService.h"
#include <cassert>
#include <stdexcept>
#include <cstring>
#include <string>
#include "comparator.h"

void Tests::testsDomain() {
    Movie m = Movie("The last of us", "Drama", 2015, 1000, "link");

    assert(m.getTitle() == "The last of us");
    assert(m.getGenre() == "Drama");
    assert(m.getYear() == 2015);
    assert(m.getNumberOfLikes() == 1000);
    assert(m.getTrailer() == "link");

    m.setNumberOfLikes(100);
    assert(m.getNumberOfLikes() == 100);

    assert(m == Movie("The last of us", "Drama", 2015, 100, "link"));

    std::string str = m.toString();
    assert(str == "Title: The last of us | Genre: Drama | Year: 2015 | Number of likes: 100 | Trailer link: link");


}

void Tests::testsVector()
{
    auto * v1 = new DynamicVector<TElem>(1);
    assert(v1->getCapacity() == 1);
    assert(v1->getSize() == 0);
    try
    {
        auto* v1Invalid = new DynamicVector<TElem>(0);
    }
    catch(const char*msg)
    {
        assert(strcmp(msg, "Can t have an array with less than an element!") == 0);
    }
    TElem elem1 = Movie("The last of us1", "Drama", 2015, 100, "link");
    v1->addVector(elem1);
    assert(v1->getSize() == 1);
    TElem elem2 = Movie("The last of us2", "Drama", 2015, 100, "link");
    v1->addVector(elem2);
    assert(v1->getSize() == 2);
    assert(v1->getCapacity() == 11);
    TElem elem3 = Movie("The last of us3", "Drama", 2015, 100, "link");
    v1->updateVector(1, elem3);
    assert(v1->getVector()[1] == elem3);
    TElem elem4 = Movie("The last of us4", "Drama", 2015, 100, "link");
    v1->addVector(elem4);
    v1->removeVector(1);
    assert(v1->getSize() == 2);
    assert(v1->getVector()[1] == elem4);

}

void Tests::testsAdminRepository() {
    auto * v1 = new DynamicVector<Movie>(10);
    Repository repo = Repository(v1);
    repo.initialiseRepo();
    assert(repo.getSize() == 10);
    assert(repo.getCapacity() == 10);
    assert(repo.getRepo()[0].getTitle() == "The Shawshank Redemption");
    Movie movie11 = Movie("idk", "idk", 10, 10, "idk");
    repo.addRepo(movie11);
    assert(repo.getSize() == 11);
    assert(repo.getCapacity() == 20);
    assert(repo.findByTitle("Schindler's List") == 5);
    repo.removeRepo(4);
    assert(repo.getSize() == 10);
    Movie movie12 = Movie("idk1", "idk1", 11, 12, "idk1");
    repo.updateRepo(9, movie12);
    assert(repo.getRepo()[9].getTitle() == "idk1");
    assert(repo.getRepo()[9].getYear() == 11);



}

void Tests::testsAdminService() {
    auto *dynamicVector = new DynamicVector<Movie>(10);
    auto *repo = new Repository(dynamicVector);
    repo->initialiseRepo();
    Service service = Service(repo);
    assert(service.getAllService()[0].getTitle() == "The Shawshank Redemption");
    assert(service.getCapacityService() == 10);
    assert(service.getSizeService() == 10);
    int added = service.addService("idk", "idk", 10, 10, "idk");
    assert(added == 0);
    assert(service.getSizeService() == 11);
    assert(service.getCapacityService() == 20);
    added = service.addService("idk", "idk", 10, 10, "idk");
    assert(added == 1);
    int deleted = service.removeService("The Shawshank Redemption");
    assert(deleted == 0);
    assert(service.getSizeService() == 10);
    deleted = service.removeService("Jim");
    assert(deleted == 1);
    int updated = service.updateService("idk", "idk1", "idk1", 11, 12, "idk1");
    assert(updated == 0);
    updated = service.updateService("idk", "idk1", "idk1", 11, 12, "idk1");
    assert(updated == 1);

}

void Tests::testsUserRepository()
{
    auto * v1 = new DynamicVector<Movie>(2);
    UserRepository userRepository = UserRepository(v1);
    assert(userRepository.getCapacity() == 2);
    Movie movie1 = Movie("idk", "idk", 10, 10, "idk");
    Movie movie2 = Movie("idk1", "idk1", 11, 12, "idk1");
    userRepository.addUserRepo(movie1);
    assert(userRepository.getSize() == 1);
    userRepository.addUserRepo(movie2);
    assert(userRepository.getAllUsersRepo()[0].getYear() == 10);
    assert(userRepository.getAllUsersRepo()[1].getTitle() == "idk1");
    userRepository.removeUserRepo(0);
    assert(userRepository.getAllUsersRepo()[0].getTitle() == "idk1");
    assert(userRepository.getSize() == 1);

    assert(userRepository.findByTitle("idk1") == 0);
}

void Tests::testsUserService()
{
    auto * v1 = new DynamicVector<Movie>(10);
    auto * repo = new Repository(v1);
    repo->initialiseRepo();
    auto * v2 = new DynamicVector<Movie>(10);
    auto * userRepo = new UserRepository(v2);
    UserService userService = UserService(repo, userRepo);

    assert(userService.getSizeService() == 0);
    assert(userService.getCapacityService() == 10);
    Movie movie = repo->getRepo()[0];
    userService.addUserService(movie);

    assert(userService.getSizeService() == 1);
    assert(userService.getAllUsersService()[0].getTitle() == "The Shawshank Redemption");

    std:: string removeName = "The Shawshank Redemption";
    userService.removeUserService(removeName);

    assert(userService.getSizeService() == 0);

    userService.addUserService(movie);

    Movie * validMovies1 = new Movie[10];
    std::string empty;
    empty[0] == '\0';
    int counter1 = userService.getFiltered(validMovies1, empty);
    assert(counter1 == 10);

    Movie * validMovies2 = new Movie[10];
    int counter2 = userService.getFiltered(validMovies2, "Crime, Drama");
    assert(counter2 == 2);
}

void Tests::testsSort() {


    std::vector<Movie> vector;

    Movie m1 = Movie("The Shawshank Redemption", "Drama", 1994, 2563415,
                     "https://www.imdb.com/video/vi3877612057?playlistId=tt0111161&ref_=tt_ov_vi");
    Movie m2 = Movie("The Godfather", "Drama, Crime", 1972, 1764309,
                     "https://www.imdb.com/video/vi1348706585?playlistId=tt0068646&ref_=tt_ov_vi");
    Movie m3 = Movie("The Dark knight", "Action, Crime, Drama", 2008, 2525427,
                     "https://www.imdb.com/video/vi324468761?playlistId=tt0468569&ref_=tt_ov_vi");
    vector.push_back(m1);
    vector.push_back(m2);
    vector.push_back(m3);

    Comparator<Movie>* c = new ComparatorAscendingByLikes{};
    Comparator<Movie>* c2 = new ComparatorAscendingByGenre{};
    sortElements(vector, c);

    assert(vector[0].getNumberOfLikes() == 1764309);
    assert(vector[1].getNumberOfLikes() == 2525427);
    assert(vector[2].getNumberOfLikes() == 2563415);

    sortElements(vector, c2);
    assert(vector[0].getGenre() == "Action, Crime, Drama");
    assert(vector[1].getGenre() == "Drama");
    assert(vector[2].getGenre() == "Drama, Crime");

    delete c;
    delete c2;
}

