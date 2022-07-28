#pragma once

#include "repository.h"

class Service{
private:
    Repository* repo;
public:

    explicit Service(Repository* repo);

    int getSizeService() { return this->repo->getSizeRepo();}

    int getCapacityService() { return this->repo->getCapacityRepo();}

    Task* getAllService() { return this->repo->getRepo();}

    ///This function gets a description, a duration and priority and it returns 1 if the task is already in the repository
    ///and 0 otherwise and adds the Task to the repository
    int addService(const std::string& description, int duration, int priority);

    ///This function filters the repository and creates a new vector of tasks only with the ones that have the priority
    /// smaller than the given one. After that it sorts the vector. It returns the number of elements form the created vector
    int filtered(int priority, Task* task);

    ~Service() = default;

};
