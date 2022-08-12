//
// Created by Aurelian on 06/04/2022.
//

#include "repository.h"

Repository::Repository(DynamicVector<Protein> *dynamicVector) {
    this->database = dynamicVector;
}

void Repository::initialiseRepo() {
    Protein p1 = Protein("Human", "Myosin-2", "ABCDEF");
    Protein p2 = Protein("Human", "Keratin", "ABCDEF");
    Protein p3 = Protein("Mouse", "Keratin", "ABCDEF");
    Protein p4 = Protein("E_Coli", "tufA", "VTLNDASFMNDSAFIW");
    Protein p5 = Protein("E_Coli", "cspE", "FDSAFJWQKFADF");

    this->database->addVector(p1);
    this->database->addVector(p2);
    this->database->addVector(p3);
    this->database->addVector(p4);
    this->database->addVector(p5);
}

void Repository::removeRepo(int index) {
    this->database->removeVector(index);
}

int Repository::findByOrganismAndName(const std::string organism,const std::string name)
{
    int index = -1;

    for(int i = 0 ; i< this->database->getSize(); i++)
    {
        if(this->database->getVector()[i].getOrganism() == organism && this->database->getVector()[i].getName() == name) {
            index = i;
        }
    }
    return index;
}


