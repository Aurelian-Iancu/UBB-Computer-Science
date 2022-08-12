

#include "domain.h"

TopScorer::TopScorer(const std::string& name, const std::string& nationality, const std::string& team, int nOfGoals) :
name{ name }, nationality{ nationality }, team{ team }, nOfGoals { nOfGoals }{}

bool TopScorer::operator==(const TopScorer& topScorer) {
    if(this->name != topScorer.name)
        return false;
    if(this->nationality != topScorer.nationality)
        return false;
    if(this->team != topScorer.team)
        return false;
    if(this->nOfGoals != topScorer.nOfGoals)
        return false;
    return true;
}

std::string TopScorer::toString() const{
    auto strNrGoals = std::to_string(this->nOfGoals);

    return this->name + " | " + this->nationality + " | " + this->team + " | " + strNrGoals;
}


