#pragma once
#include <string>

class User{
private:
    std::string name;
    std::string type;
public:
    User(): name{""}, type{""}{}

    User(const std::string& name,const std::string& type);

    std::string getName() { return this-> name;}

    std::string getType() {return this->type;}

    ~User() = default;
};

class Issue{
private:
    std::string description;
    std::string status;
    std::string reporter;
    std::string solver;

public:
    Issue(): description{""}, status{"open"}, reporter{""}, solver{"none"}{}

    Issue(const std::string& description,const std::string& status,const std::string& reporter,const std::string& solver);

    std::string getDescription(){return this->description;};

    std::string getStatus(){return this->status;};

    std::string getReported(){return this->reporter;};

    std::string getSolver() {return this->solver;};

    std::string toString();

    ~Issue() = default;
};