#pragma once

#include "MedicalAnalysis.h"
#include <vector>

class Person{
private:
    std::string name;
    std::vector<MedicalAnalysis*> v;
public:
    Person(std::string name);

    void addAllAnalysis(const std::string& BMIFilename,const std::string& BPFilename);

    std::vector<MedicalAnalysis*> getAllAnalysis();

    std::vector<MedicalAnalysis*> getALlAnalysisBetweenDates(std::string date1, std::string date2);

    void writeToFile(std::string filename, std::string date1, std::string date2);

    ~Person();


};
