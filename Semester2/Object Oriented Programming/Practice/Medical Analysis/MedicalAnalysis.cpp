

#include "MedicalAnalysis.h"
#include <iostream>

MedicalAnalysis::MedicalAnalysis(const std::string& date) {
    this->date = date;
}

std::string MedicalAnalysis::toString() const {
    return date;
}

std::istream &operator>>(std::istream &is, MedicalAnalysis &a) {
    return a.read(is);
}

std::ostream &operator<<(std::ostream &os, MedicalAnalysis &a) {
    os << a.toString() << std::endl;
    return os;
}
