

#include "Person.h"
#include <fstream>
#include "BP.h"
#include "BMI.h"
Person::Person(std::string name): name { name }{}

void Person::addAllAnalysis(const std::string& BMIFilename,const std::string& BPFilename) {
    std::ifstream f{BMIFilename};

    BMI bmi{};
    while(f >> bmi)
    {
        MedicalAnalysis* a = new BMI {bmi};
        this->v.push_back(a);
    }

    std::ifstream g{BPFilename};

    BP bp{};
    while(g >> bp)
    {
        MedicalAnalysis* b = new BP {bp};
        this->v.push_back(b);
    }
}

Person::~Person()
{
    for (auto e : this->v)
    {
        delete e;
    }
}

std::vector<MedicalAnalysis *> Person::getAllAnalysis() {
    return this->v;
}

