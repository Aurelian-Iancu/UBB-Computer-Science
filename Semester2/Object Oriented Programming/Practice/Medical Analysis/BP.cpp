

#include "BP.h"
#include <sstream>
#include <vector>
#include "Utils.h"

BP::BP(): MedicalAnalysis(""), systolicValue(0), diastolicValue(0) {}

BP::BP(const std::string& date, int systolicValue, int diastolicValue): MedicalAnalysis{date}, systolicValue{systolicValue},
    diastolicValue{diastolicValue}{}

bool BP::isResultOK() const {
    if((systolicValue >= 90 && systolicValue <=119) && (diastolicValue >= 60 && diastolicValue <= 79))
        return true;
    return false;
}

std::string BP::toString() const {
    std::stringstream ss;
    ss << date << " " <<  systolicValue << " " << diastolicValue;
    return ss.str();
}

std::istream &BP::read(std::istream &is) {
    std::string line;
    std::getline(is, line);

    std::vector<std::string> tokens = tokenize(line, ',');
    if(tokens.size() != 3)
        return is;

    this->date = tokens[0];
    this->systolicValue = std::stoi(tokens[1]);
    this->diastolicValue = std::stoi(tokens[2]);
    return is;
}



