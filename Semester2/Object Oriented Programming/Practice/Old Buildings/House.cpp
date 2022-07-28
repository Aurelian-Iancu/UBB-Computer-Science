//
// Created by Aurelian on 03/05/2022.
//

#include "House.h"

House::House() {

}

House::~House() {

}

House::House(const std::string &address,const int &constructionYear,const bool& isHistorical):
Building(address, constructionYear), isHistorical(isHistorical){

}

bool House::mustBeRestored() {
    if(2022 - this->constructionYear > 100)
        return true;
    return false;
}

bool House::canBeDemolished() {
    if(!isHistorical)
        return true;
    return false;
}

std::string House::toString() {
    std::stringstream ss;
    ss << address << " " << constructionYear << " " << isHistorical;
    return ss.str();
}

