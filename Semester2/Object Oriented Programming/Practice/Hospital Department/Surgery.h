#pragma once

#include <sstream>
#include <string>
#include "HospitalDepartment.h"

class Surgery: public HospitalDepartment {
private:
    int numberOfPatients;
public:
    Surgery();

    Surgery(const std::string& hospitalName, const int & numberOfDoctors, const int& numberOfPatients);

    bool isEfficient() override;

    std::string toString() override;

    ~Surgery() = default;
};