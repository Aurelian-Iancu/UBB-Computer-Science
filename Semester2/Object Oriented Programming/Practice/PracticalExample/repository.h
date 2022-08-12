#pragma once
#include <vector>
#include "domain.h"

class Repository{
private:
    std::vector<Issue> issues;
    std::string userFile;
    std::vector<User*> users;
    std::string issueFile;

public:
    Repository(std::vector<Issue>& issues, std::vector<User*>& users, std::string& issueFile, std::string& userFile);

    std::vector<Issue> getAllIssuesRepo();

    std::vector<User*> getAllUsersRepo();

    std::string getIssuesFileRepo();

    std::string getUserFileRepo();

    void tokenizeUser(std::string readString);

    void loadFromFileUser();

    void tokenizeIssue(std::string readString);

    void loadFromFileIssue();

    void initialiseRepo();

    int findByDescription(const std::string& description);

    /// searches in the repo to see if you can find the title. If yes, throw exception, else adds it to the vector
    /// \param issue the issue to be added
    void addIssueRepo(Issue& issue);

    void removeIssueRepo(int index);

    void updateIssueRepo(int index, Issue& newIssue);

    void writeIssuesToFile();

    void writeToFileRepo();

    ~Repository() = default;
};
