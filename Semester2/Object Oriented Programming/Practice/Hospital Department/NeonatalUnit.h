#pragma once

#include <sstream>
#include <string>
#include "HospitalDepartment.h"

class NeonatalUnit: public HospitalDepartment
{
private:
    int numberOfMothers;
    int numberOfNewborns;

public:
    double averageGrade;

    NeonatalUnit();

    NeonatalUnit(const std::string& hospitalName, const int& numberOfDocs, const int& numberOfMoms, const int& numbersOfNewborns, const double& averageGrade);

    bool isEfficient() override;

    std::string toString() override;

    ~NeonatalUnit() = default;


};