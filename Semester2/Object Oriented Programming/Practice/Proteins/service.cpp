//
// Created by Aurelian on 06/04/2022.
//

#include "service.h"

Service::Service(Repository *repo) {
    this->repo = repo;
}

int Service::removeService(const std::string organism, const std::string name) {
    int delete_index = this->repo->findByOrganismAndName(organism, name);

    if(delete_index == -1)
        return 0;
    else
    {
        this->repo->removeRepo(delete_index);
        return 1;
    }
}

int Service::filter(const std::string &sequence, Protein *result) {
    int length = this->repo->getSizeRepo();

    int lengthResult = 0;

    for(int i = 0; i < length; i++)
    {
        if(this->repo->getRepo()[i].getSequence() == sequence)
        {
            result[lengthResult] = this->repo->getRepo()[i];
            lengthResult++;
        }
    }

    for(int i = 0; i < lengthResult - 1; i++)
        for(int j = i+1; j < lengthResult; j++)
        {
            if(result[i].getName() > result[j].getName())
            {
                auto aux = result[i];
                result[i] = result[j];
                result[j] = aux;
            }
        }
    return lengthResult;
}



