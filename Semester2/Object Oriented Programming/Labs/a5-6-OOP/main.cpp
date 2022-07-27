#include "repository.h"
#include "dynamicVector.h"
#include "service.h"
#include "ui.h"
#include "movie.h"
#include <iostream>
#include "tests.h"


void tests()
{
    Tests t;
    t.testsDomain();
    t.testsAdminRepository();
    t.testsAdminService();
    t.testsVector();
    t.testsUserRepository();
    t.testsUserService();
    t.testsSort();
    std::cout << "All tests passed successfully!\n";

}

int main()
{


    auto * dynamicVector = new DynamicVector<Movie>(10);
    auto * repo = new Repository(dynamicVector);
    repo->initialiseRepo();
    auto * dynamicVector1 = new DynamicVector<Movie>(10);
    auto *userRepo = new UserRepository(dynamicVector1);

    auto * service = new Service(repo);
    auto * userService = new UserService(repo, userRepo);
    auto * ui = new UI(service, userService);

    tests();

    ui->start();


    return 0;
}

