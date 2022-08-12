//
// Created by Aurelian on 04/06/2022.
//

#include "domain.h"

User::User(const std::string &name,const std::string &type) {
    this->name = name;
    this->type = type;
}

Issue::Issue(const std::string &description,const std::string &status,const std::string &reporter,const std::string &solver) {
    this->description = description;
    this->status = status;
    this->reporter = reporter;
    this->solver = solver;
}

std::string Issue::toString() {
    return this->description + " " + this->status + " " + this->reporter + " " + this->solver;
}
