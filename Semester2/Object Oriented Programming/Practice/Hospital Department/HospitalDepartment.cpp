

#include "HospitalDepartment.h"
#include <sstream>

std::string HospitalDepartment::toString() {
    std::stringstream ss;
    ss << hospitalName << " " << numberOfDoctors;
    return ss.str();
}

HospitalDepartment::HospitalDepartment(const std::string& hospitalName,const int& numberOfDoctors)
{
    this->hospitalName = hospitalName;
    this->numberOfDoctors = numberOfDoctors;
}

HospitalDepartment::HospitalDepartment() {}

std::string HospitalDepartment::getName() {
    return this->hospitalName;
}

