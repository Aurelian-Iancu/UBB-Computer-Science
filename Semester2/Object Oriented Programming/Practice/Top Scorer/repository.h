#pragma once

#include "dynamicVector.h"
#include "domain.h"

class Repository{
private:
    DynamicVector<TopScorer>* database;

public:
    explicit Repository(DynamicVector<TopScorer>* repoArray);

    ~Repository() = default;

    int getSizeRepo() {return this->database->getSize();}

    int getCapacityRepo() { return this->database->getCapacity();}

    TopScorer* getRepo() { return this->database->getVector();}

    void addRepo(TopScorer& topScorer);

    void initialiseRepo();
};
