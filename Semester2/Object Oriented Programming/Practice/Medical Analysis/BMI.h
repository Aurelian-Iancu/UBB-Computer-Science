#pragma once
#include "MedicalAnalysis.h"

class BMI: public MedicalAnalysis
{
private:
    double value;
public:

    BMI();

    BMI(const std::string& date, double value);

    bool isResultOK()const override;

    std::string toString() const override;

    std::istream& read(std::istream& is) override;

    ~BMI() = default;
};
