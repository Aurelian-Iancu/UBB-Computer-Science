#pragma once

#include "dynamicVector.h"

class Repository{
private:
    DynamicVector<Task>* database;

public:
    explicit Repository(DynamicVector<Task>* dynamicVector);

    void initialiseRepo();

    int getSizeRepo(){return this->database->getSize();}

    int getCapacityRepo() {return this->database->getCapacity();}

    Task* getRepo() {return this->database->getVector();}

    ///This function calls the add function from the dynamic vector to add a task
    void addRepo(Task& task);

    ~Repository() = default;

};