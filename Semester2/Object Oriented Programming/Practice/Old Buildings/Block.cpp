//
// Created by Aurelian on 03/05/2022.
//

#include "Block.h"
#include "Building.h"
#include <sstream>

Block::Block(){

}

Block::Block(const std::string& address,const int& constructionYear,const int& totalApartments,const int& occupiedApartments)
:Building(address, constructionYear), totalApartments(totalApartments), occupiedApartments(occupiedApartments){

}

bool Block::mustBeRestored() {
    if((2022- this->constructionYear > 40) && (this->occupiedApartments > 0.8 * totalApartments))
        return true;
    return false;
}

bool Block::canBeDemolished() {
    if(this->occupiedApartments < 0.05 * this->totalApartments)
        return true;
    return false;
}

std::string Block::toString() {
    std::stringstream ss;
    ss << this->address << " " << this->constructionYear << " " << this->totalApartments << " " << this->occupiedApartments;
    return ss.str();
}

