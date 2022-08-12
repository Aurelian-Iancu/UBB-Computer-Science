//
// Created by Aurelian on 06/04/2022.
//

#include "domain.h"

Protein::Protein(const std::string organism, const std::string name, const std::string sequence):
organism{ organism }, name { name }, sequence{ sequence }{}

std::string Protein::toString() {
    return this->organism + " | " + this->name + " | " + this->sequence;
}



