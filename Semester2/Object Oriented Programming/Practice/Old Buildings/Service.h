#pragma once

#include "Building.h"
#include "Block.h"
#include "House.h"
#include <vector>
#include <string>

class Service{
private:
    std::vector<Building*> vector;
public:
    Service();

    void addBuilding(Building *building);

    std::vector<Building*> getAllBuildings();

    std::vector<Building*> getAllToBeRestored();

    std::vector<Building*> getAllToBeDemolished();

    void writeToFile(std::string filename, std::vector<Building*> buildings);

    ~Service();
};
