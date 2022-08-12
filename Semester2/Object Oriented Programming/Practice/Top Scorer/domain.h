#pragma once
#include <string>

class TopScorer
{
private:
    std::string name;
    std::string nationality;
    std::string team;
    int nOfGoals;

public:
    TopScorer(): name{""}, nationality{""}, team{""}, nOfGoals{0}{}

    TopScorer(const std::string& name, const std::string& nationality, const std::string& team, int nOfGoals);

    std::string getName(){return this->name;}

    std::string getNationality(){ return this->nationality;}

    std::string getTeam() const { return this-> team;}

    int getNumberOfGoals() const { return this->nOfGoals;}

    bool operator==(const TopScorer& topScorer);

    std::string toString() const;
};
