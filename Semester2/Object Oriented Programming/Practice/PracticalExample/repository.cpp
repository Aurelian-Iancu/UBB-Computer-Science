

#include "repository.h"
#include <fstream>
#include <sstream>
#include <algorithm>

Repository::Repository(std::vector<Issue> &issues, std::vector<User*> &users, std::string &issueFile,
                       std::string &userFile) {
    this->issues = issues;
    this->users = users;
    this->issueFile = issueFile;
    this->userFile = userFile;
}

std::vector<Issue> Repository::getAllIssuesRepo() {
    return this->issues;
}

std::vector<User*> Repository::getAllUsersRepo() {
    return this->users;
}

std::string Repository::getIssuesFileRepo() {
    return this->issueFile;
}

std::string Repository::getUserFileRepo() {
    return this->userFile;
}

void Repository::tokenizeUser(std::string readString)
{
    std::string items[10];
    int index = 0;
    std::stringstream ss(readString);
    std:: string word;
    while(ss >> word)
    {
        items[index] = word;
        index++;
    }
    User* userToAdd = new User{items[0], items[1]};
    this->users.push_back(userToAdd);
}

void Repository::loadFromFileUser() {
    if(!this->userFile.empty())
    {
        User userFromFile;
        std::ifstream fin(this->userFile);
        std::string readString;
        User readUser;
        while(std::getline(fin, readString))
        {
            fin.clear();
            this->tokenizeUser(readString);
        }
    }
}

void Repository::tokenizeIssue(std::string readString)
{
    std::string items[10];
    int index = 0;
    std::stringstream ss(readString);
    std:: string word;
    while(ss >> word)
    {
        items[index] = word;
        index++;
    }
    Issue issueToAdd{items[0], items[1], items[2], items[3]};
    this->issues.push_back(issueToAdd);
}

void Repository::loadFromFileIssue() {
    if(!this->issueFile.empty())
    {
        std::ifstream fin(this->issueFile);
        std::string readString;
        while(std::getline(fin, readString))
        {
            fin.clear();
            this->tokenizeIssue(readString);
        }
    }
}

void Repository::initialiseRepo() {
    this->loadFromFileIssue();
    this->loadFromFileUser();
}

int Repository::findByDescription(const std::string& description){
    int searchedIndex = -1;
    auto it = std::find_if(this->issues.begin(), this->issues.end(), [&description](Issue& issue){return issue.getDescription() == description;});
    if(it != this->issues.end())
        searchedIndex = it - this->issues.begin();
    return searchedIndex;
}

void Repository::addIssueRepo(Issue& issue) {
    int existing = this->findByDescription(issue.getDescription());
    if(existing != -1)
    {
        throw "The Issue is already in the list";
    }
    this->issues.push_back(issue);
    this->writeIssuesToFile();
}

void Repository::removeIssueRepo(int index)
{
    if(index == -1)
        throw "The Issue is not in the list";
    this->issues.erase(this->issues.begin() + index);
    this->writeIssuesToFile();
}

void Repository::writeIssuesToFile() {
    if(!this->issueFile.empty())
    {
        std::ofstream fout(this->issueFile);
        for(auto movie: this->issues)
        {
            fout << movie.toString() << "\n";
        }
        fout.close();
    }
}

void Repository::updateIssueRepo(int index, Issue& newIssue){
    if(index == -1)
    {
        throw "The Issue does not exist";
    }
    this->issues[index] = newIssue;
    this->writeIssuesToFile();
}

void Repository::writeToFileRepo() {
    this->writeIssuesToFile();
}






