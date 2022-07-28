#pragma once

#include <string>

class Building{
protected:
    std::string address;
    int constructionYear;

public:
    Building();

    Building(const std::string& address,const int& constructionYear);

    virtual bool mustBeRestored()=0;

    virtual bool canBeDemolished()=0;

    virtual std::string toString();

    virtual ~Building() = default;

    int getYear();

};