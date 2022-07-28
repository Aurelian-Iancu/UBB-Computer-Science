

#include "repository.h"

Repository::Repository(DynamicVector<Task> *dynamicVector) {
    this->database = dynamicVector;

}


void Repository::addRepo(Task& task) {
    this->database->addVector(task);
}

void Repository::initialiseRepo() {
    Task t1 = Task("Solve_OOP_assignment", 120, 1);
    Task t2 = Task("Respond to emails", 45, 2);
    Task t3 = Task("Eat_sushi", 30, 3);
    Task t4 = Task("Visit_parent", 240, 1);
    Task t5 = Task("Buy_a_jacket", 120, 2);
    this->database->addVector(t1);
    this->database->addVector(t2);
    this->database->addVector(t3);
    this->database->addVector(t4);
    this->database->addVector(t5);
}

