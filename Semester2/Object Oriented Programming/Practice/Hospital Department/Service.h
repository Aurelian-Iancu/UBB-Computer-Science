#pragma once

#include <string>
#include <vector>
#include "HospitalDepartment.h"


class Service{
private:
    std::vector<HospitalDepartment*> vector;

public:
    Service();

    ~Service();

    void addDepartment(HospitalDepartment* hospitalDepartment);

    std::vector<HospitalDepartment*> getAll();

    std::vector<HospitalDepartment*> getAllEfficient();

    void writeToFile(std::string& filename);

};
