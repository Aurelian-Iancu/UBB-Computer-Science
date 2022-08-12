//
// Created by Aurelian on 04/04/2022.
//

#include "service.h"

Service::Service(Repository *repo) {
    this->repo = repo;
}

int Service::addService(const std::string& name,const std::string& nationality,const std::string& team, int nOfGoals) {
    int found = 0;
    int index;
    TopScorer topScorer;

    for(index = 0; index <= this->getSizeService(); index++)
        if(this->getAllService()[index].getName() == name)
            found = 1;

    topScorer = TopScorer(name, nationality, team, nOfGoals);
    this->repo->addRepo(topScorer);

    return found;
}

int Service::filter(const std::string &team, TopScorer* result) {
    int length = this->repo->getSizeRepo();

    int lengthResult = 0;

    for(int i = 0; i < length; i++)
        if(this->getAllService()[i].getTeam() == team) {
            result[lengthResult] = this->getAllService()[i];
            lengthResult++;
        }

    for(int i = 0; i < lengthResult - 1; i++)
        for(int j = i+1; j < lengthResult; j++)
            if(result[i].getNumberOfGoals() < result[j].getNumberOfGoals())
            {
                auto aux = result[i];
                result[i] = result[j];
                result[j] = aux;
            }
    return lengthResult;
}

