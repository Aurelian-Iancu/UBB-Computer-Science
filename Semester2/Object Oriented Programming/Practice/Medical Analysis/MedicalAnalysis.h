#pragma once

#include <string>

class MedicalAnalysis {
protected:
    std::string date;
public:
    explicit MedicalAnalysis(const std::string& date);

    virtual bool isResultOK()const = 0;

    virtual std::string toString() const;

    virtual std::istream& read(std::istream& is) = 0;

    virtual ~MedicalAnalysis() = default;

    friend std::istream& operator>>(std::istream& is, MedicalAnalysis& a);

    friend std::ostream& operator<<(std::ostream& os, MedicalAnalysis& a);

};
