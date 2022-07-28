

#include "Service.h"
#include <fstream>
#include <iostream>

Service::Service() {

}

std::vector<Building *> Service::getAllBuildings() {
    return this->vector;
}

std::vector<Building *> Service::getAllToBeRestored() {
    std::vector<Building*> vector1;
    for(auto &building: this->vector)
    {
        if(building->mustBeRestored())
            vector1.push_back(building);
    }
    return vector1;
}

std::vector<Building *> Service::getAllToBeDemolished() {
    std::vector<Building*> vector1;
    for(auto &building: this->vector)
    {
        if(building->canBeDemolished())
            vector1.push_back(building);
    }
    return vector1;
}

void Service::writeToFile(std::string filename, std::vector<Building *> buildings) {
    std::ofstream fout(filename);

    for(auto &building: buildings)
    {
        fout << building->toString() << std::endl;
    }
}

Service::~Service() {
    for(auto &i: this->vector)
    {
        delete i;
    }
}

void Service::addBuilding(Building *building) {
    this->vector.push_back(building);
}



