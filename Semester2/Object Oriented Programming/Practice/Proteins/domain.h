#pragma once
#include <string>

class Protein{
private:
    std::string organism;
    std::string name;
    std::string sequence;

public:
    Protein(): organism{""}, name{""}, sequence{""}{}

    Protein(const std::string organism, const std::string name, const std::string sequence );

    std::string getOrganism(){return this->organism;}
    std::string getName(){ return this->name;}
    std::string getSequence() { return this->sequence;}

    std::string toString();
};
