#pragma once

#include "dynamicVector.h"
#include "domain.h"

class Repository{
private:
    DynamicVector<Protein>* database;

public:
    Repository(DynamicVector<Protein>* dynamicVector);

    ~Repository() = default;

    int getSizeRepo() { return this->database->getSize();}

    Protein* getRepo() { return this->database->getVector();}

    void initialiseRepo();

    ///This function removes an element from a certain index in repo by calling removeVector from the dynamic Array;
    void removeRepo(int index);

    int findByOrganismAndName(const std::string organism, const std::string name);
};
