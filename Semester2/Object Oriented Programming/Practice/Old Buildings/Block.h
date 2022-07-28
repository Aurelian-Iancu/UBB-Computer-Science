#pragma once
#include "Building.h"
#include <string>

class Block: public Building
{
private:
    int totalApartments;
    int occupiedApartments;
public:
    Block();

    Block(const std::string& address,const int& constructionYear,const int& totalApartments,const int& occupiedApartments);

    bool mustBeRestored() override;

    bool canBeDemolished() override;

    std::string toString() override;

    ~Block() = default;

};
