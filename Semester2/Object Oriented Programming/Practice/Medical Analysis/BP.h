#pragma once
#include "MedicalAnalysis.h"

class BP:public MedicalAnalysis{
private:
    int systolicValue;
    int diastolicValue;

public:
    BP();

    BP(const std::string& date, int systolicValue, int diastolicValue);

    bool isResultOK() const override;

    std::string toString() const override;

    std::istream& read(std::istream& is) override;

    ~BP() = default;
};
