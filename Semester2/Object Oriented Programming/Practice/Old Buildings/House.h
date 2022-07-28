#pragma once

#include <string>
#include <sstream>
#include "Building.h"

class House: public Building
{
private:
    bool isHistorical;
public:
    House();

    House(const std::string& address,const int& constructionYear,const bool& isHistorical);

    bool mustBeRestored() override;

    bool canBeDemolished() override;

    std::string toString() override;

    ~House();
};
