#pragma once

#include <string>

class HospitalDepartment{
protected:
    std::string hospitalName;
    int numberOfDoctors;

public:
    HospitalDepartment();

    HospitalDepartment(const std::string& hospitalName,const int& numberOfDoctors);

    virtual ~HospitalDepartment() = default;

    virtual bool isEfficient() = 0;

    virtual std::string toString();

    std::string getName();
};
