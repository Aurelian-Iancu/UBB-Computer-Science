#pragma once

#include "repository.h"

class Service{
private:
    Repository* repo;

public:
    Service(Repository* repo);

    ~Service() = default;

    int getSizeService(){ return this->repo->getSizeRepo();}

    Protein* getAllService() {return this->repo->getRepo();}

    ///This function uses the function find to get the index of the element that has a certain organism and name
    ///If we find the Protein the function will return 1, 0 otherwise;
    int removeService(const std::string organism, const std::string name);

    ///In this function we filter the repository into the vector of proteins result only with the Proteins that have
    ///a certain sequence. After that we sort the result by name. We return the length of result
    int filter(const std::string& sequence, Protein* result);

};