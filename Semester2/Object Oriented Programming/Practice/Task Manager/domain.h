#pragma once

#include <string>

class Task
{
private:
    std::string description;
    int duration;
    int priority;

public:
    explicit Task(): description{""}, duration{0}, priority{0}{}

    Task(const std::string& description, int duration, int priority);

    std::string getDescription() { return this->description;}

    int getDuration() const { return this->duration; }

    int getPriority() const { return this->priority; }

    std::string toString();

    ~Task() = default;

};
