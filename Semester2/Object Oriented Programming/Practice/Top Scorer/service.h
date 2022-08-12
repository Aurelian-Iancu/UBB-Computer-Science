#pragma once

#include "repository.h"

class Service{
private:
    Repository* repo;

public:
    explicit Service(Repository *repo);

    ~Service() = default;

    int getSizeService(){ return this->repo->getSizeRepo();}

    int getCapacityService() { return this->repo->getCapacityRepo();}

    TopScorer* getAllService() { return this->repo->getRepo();}


    int addService(const std::string& name,const std::string& nationality,const std::string& team, int nOfGoals);

    int filter(const std::string &team, TopScorer* result);
};
