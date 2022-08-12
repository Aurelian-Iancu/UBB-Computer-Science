//
// Created by Aurelian on 04/06/2022.
//

#include "service.h"
#include "algorithm"

bool sortIssue(Issue issue1, Issue issue2)
{
    if(issue1.getStatus() < issue2.getStatus())
        return true;
    else if(issue1.getStatus() == issue2.getStatus() && issue1.getDescription() < issue2.getDescription())
        return true;
    else
        return false;
}

Service::Service(Repository& repository1):repository(repository1) {

}

std::vector<Issue> Service::getAllIssuesService() {
    return this->repository.getAllIssuesRepo();
}

std::vector<User*> Service::getAllUsersService() {
    return this->repository.getAllUsersRepo();
}

std::vector<Issue> Service::getAllIssuesSorted() {
    std::vector<Issue> vector;
    vector = this->repository.getAllIssuesRepo();
    std::sort(vector.begin(), vector.end(), sortIssue);
    return vector;
}

void Service::addIssueService(const std::string &description, const std::string &status, const std::string& reporter, const std::string& solver) {
    Issue issue = Issue(description, status, reporter, solver);
    this->repository.addIssueRepo(issue);
    notify();
}

void Service::removeIssueService(std::string &title) {
    int deleteIndex = this->repository.findByDescription(title);
    Issue issue = this->repository.getAllIssuesRepo()[deleteIndex];
    this->repository.removeIssueRepo(deleteIndex);
    this->notify();
}

void Service::updateIssueService(const std:: string& description, const std::string& newDescription, const std::string& newStatus, const std::string& newReporter, const std::string& newSolver) {
    int updateIndex = this->repository.findByDescription(description);
    Issue newIssue = Issue(newDescription, newStatus, newReporter, newSolver);
    this->repository.updateIssueRepo(updateIndex, newIssue);
    this->notify();
}




