#include "repository.h"
#include "service.h"
#include "ui.h"
#include "movie.h"
#include <vector>
#include "validators.h"
#include <crtdbg.h>

int main()
{

    std::vector<Movie> repoAdminVector;
    repoAdminVector.reserve(10);
    std::string filename = R"(C:\Users\Aurelian\Documents\GitHub\OOP\a8-9-913-Iancu-Gheorghe-Aurelian\movies.txt)";
    Repository repo{repoAdminVector, filename};
    repo.initialiseRepo();
    Service service{repo};
    std::vector<Movie> repoUserVector;
    UserService userService{repo};
    MovieValidator validator{};
    UI ui{service, userService, validator};
    ui.start();


    printf("%d", _CrtDumpMemoryLeaks());
    return 0;
}
