//
// Created by Aurelian on 05/04/2022.
//

#include "domain.h"

Task::Task(const std::string &description, int duration, int priority):
description{ description}, duration{ duration}, priority{ priority}{}

std::string Task::toString() {
    auto string_duration = std::to_string(this->duration);
    auto string_priority = std::to_string(this->priority);

    return description + " | " + string_duration + " | " + string_priority;
}

