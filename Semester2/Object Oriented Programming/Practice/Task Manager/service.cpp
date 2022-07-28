//
// Created by Aurelian on 05/04/2022.
//

#include "service.h"

Service::Service(Repository *repo) {
    this->repo = repo;

}

int Service::addService(const std::string& description, int duration, int priority) {
    int found = 0;
    int length = this->repo->getSizeRepo();

    for(int i = 0; i < length; i++)
        if(this->repo->getRepo()[i].getDescription() == description)
            found = 1;

    Task t1;
    t1 = Task(description, duration, priority);
    this->repo->addRepo(t1);

    return found;
}

int Service::filtered(int priority, Task *result) {
    int length = this->repo->getSizeRepo();

    int lengthResult = 0;

    for(int i = 0; i < length; i++)
    {
        if(this->getAllService()[i].getPriority() < priority)
        {
            result[lengthResult] = this->repo->getRepo()[i];
            lengthResult++;
        }
    }
    for(int i = 0; i < lengthResult - 1; i++)
        for(int j = i+1; j < lengthResult; j++)
        {
            if(result[i].getDuration() < result[j].getDuration())
            {
                auto aux = result[i];
                result[i] = result[j];
                result[j] = aux;
            }
        }



    return lengthResult;
}

