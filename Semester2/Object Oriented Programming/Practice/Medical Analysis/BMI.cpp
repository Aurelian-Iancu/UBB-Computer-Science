

#include "BMI.h"
#include <sstream>
#include <vector>
#include "Utils.h"

BMI::BMI(): MedicalAnalysis(""), value(0) {

}

BMI::BMI(const std::string &date, double value): MedicalAnalysis{date}, value{value} {

}

bool BMI::isResultOK() const {
    if(this->value >= 18.5 && this->value <= 25)
        return true;
    return false;
}

std::istream& BMI::read(std::istream& is)
{
    std::string line;
    getline(is, line);

    std::vector<std::string> tokens = tokenize(line, ',');
    if (tokens.size() != 2)
        return is;
    this->date = tokens[0];
    this->value = stod(tokens[1]);
    return is;
}

std::string BMI::toString() const {
    std::stringstream ss;
    ss << date << " " << value;
    return ss.str();

}



