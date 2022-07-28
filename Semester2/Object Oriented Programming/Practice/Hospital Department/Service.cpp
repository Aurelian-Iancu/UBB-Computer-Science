//
// Created by Aurelian on 04/05/2022.
//

#include "Service.h"
#include <vector>
#include <fstream>
#include <algorithm>

Service::Service() {

}

Service::~Service() {
    for(auto &i: this->vector)
        delete i;
}

void Service::addDepartment(HospitalDepartment* hospitalDepartment) {
    this->vector.push_back(hospitalDepartment);
}

std::vector<HospitalDepartment *> Service::getAll() {
    return this->vector;
}

std::vector<HospitalDepartment *> Service::getAllEfficient() {
    std::vector<HospitalDepartment*> auxiliar;

    for(auto &i: this->vector)
    {
        if(i->isEfficient())
            auxiliar.push_back(i);
    }

    return auxiliar;

}


void Service::writeToFile(std::string& filename) {
    std::ofstream fout(filename);

    std::sort(vector.begin(), vector.end(), [](HospitalDepartment* a, HospitalDepartment* b){ return a->getName() < b->getName();});

    for(auto &i: this->vector)
    {
        fout << i->toString() << " " << i->isEfficient() << std::endl;
    }
}



