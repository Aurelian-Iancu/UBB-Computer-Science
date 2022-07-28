#include "Surgery.h"


Surgery::Surgery() {}

Surgery::Surgery(const std::string &hospitalName, const int &numberOfDoctors, const int &numberOfPatients)
:HospitalDepartment(hospitalName, numberOfDoctors), numberOfPatients(numberOfPatients){}

bool Surgery::isEfficient() {
    if(numberOfPatients / numberOfDoctors >= 2)
        return true;
    return false;
}

std::string Surgery::toString() {
    std::stringstream ss;
    ss << "Surgery:" << hospitalName << " " << numberOfDoctors << " " << numberOfPatients;
    return ss.str();
}

