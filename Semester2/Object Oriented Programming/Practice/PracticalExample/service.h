#pragma once
#include "repository.h"
#include "Observer.h"

class Service: public Subject{
private:
    Repository& repository;
public:
    Service(Repository& repository1);

    ~Service() = default;

    std::vector<Issue> getAllIssuesService();

    std::vector<User*> getAllUsersService();

    std::vector<Issue> getAllIssuesSorted();

    /// In this function you just call the repo function and you notify the other observers
    /// \param description issue's description
    /// \param status issue's status
    /// \param reporter issue's reporter
    /// \param solver issue's solver
    void addIssueService(const std::string& description, const std::string& status, const std::string& reporter, const std::string& solver);

    void removeIssueService(std::string& title);

    void updateIssueService(const std:: string& description, const std::string& newDescription, const std::string& newStatus, const std::string& newReporter, const std::string& newSolver);
};