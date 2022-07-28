//
// Created by Aurelian on 03/05/2022.
//

#include "Building.h"
#include <sstream>

std::string Building::toString() {
    std::stringstream ss;
    ss << address << " " << constructionYear;
    return ss.str();
}

Building::Building(const std::string& address,const int& constructionYear) {
    this->address = address;
    this->constructionYear = constructionYear;
}

Building::Building() {

}

int Building::getYear() {
    return this->constructionYear;
}

