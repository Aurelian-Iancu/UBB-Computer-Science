//
// Created by Aurelian on 04/05/2022.
//

#include "NeonatalUnit.h"
#include "HospitalDepartment.h"

NeonatalUnit::NeonatalUnit() {}

NeonatalUnit::NeonatalUnit(const std::string &hospitalName, const int &numberOfDocs, const int &numberOfMoms,
                 const int &numbersOfNewborns, const double &averageGrade):
                 HospitalDepartment(hospitalName, numberOfDocs), numberOfMothers(numberOfMoms),
                 numberOfNewborns(numbersOfNewborns), averageGrade(averageGrade){}

bool NeonatalUnit::isEfficient() {
    if(this->averageGrade > 8.5 && this->numberOfNewborns >= this->numberOfMothers)
        return true;
    return false;
}

std::string NeonatalUnit::toString() {
    std::stringstream ss;
    ss << "Neonatal: " << hospitalName << " " << numberOfDoctors << " " << numberOfMothers << " " << numberOfNewborns << " " << averageGrade;
    return ss.str();
}





