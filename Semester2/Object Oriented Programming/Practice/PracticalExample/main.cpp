#include <iostream>
#include "QApplication"
#include "domain.h"
#include "repository.h"
#include "service.h"
#include "window.h"
#include "QWidget"
#include "tests.h"

#include "domain.h"
#include "repository.h"
#include "service.h"
#include <cassert>

void testAdd()
{
    std::vector<Issue> vectorIssues;
    std::string issueFile = R"(C:\Users\Aurelian\ClionProjects\CourseExample\issues.txt)";
    std::vector<User*> vectorUsers;
    std::string userFile = R"(C:\Users\Aurelian\ClionProjects\CourseExample\users.txt)";
    Repository repository{vectorIssues, vectorUsers, issueFile, userFile};
    repository.initialiseRepo();
    Service service{repository};

    //assert(repository.getAllIssuesRepo().size() == 5);

    Issue issue("...", "open", "Dumitru", "Dorel");
    repository.addIssueRepo(issue);
    assert(repository.getAllIssuesRepo()[5].getDescription() == issue.getDescription());
    assert(repository.getAllIssuesRepo()[5].getStatus() == issue.getStatus());
    assert(repository.getAllIssuesRepo()[5].getReported() == issue.getReported());
    assert(repository.getAllIssuesRepo()[5].getSolver() == issue.getSolver());

    std::cout << "Add tests passed";
}

int main(int argc, char* argv[]) {
    QApplication a(argc, argv);
    std::vector<Issue> vectorIssues;
    std::string issueFile = R"(C:\Users\Aurelian\ClionProjects\CourseExample\issues.txt)";
    std::vector<User*> vectorUsers;
    std::string userFile = R"(C:\Users\Aurelian\ClionProjects\CourseExample\users.txt)";
    Repository repository{vectorIssues, vectorUsers, issueFile, userFile};
    repository.initialiseRepo();
    Service service{repository};
    std::vector<Window*> windows;
    for(auto user:service.getAllUsersService())

    {
        auto window  = new Window(service, user);
        windows.push_back(window);
    }

    for(auto wnd:windows)
    {
        wnd->show();
    }

    a.exec();



    return 0;
}
