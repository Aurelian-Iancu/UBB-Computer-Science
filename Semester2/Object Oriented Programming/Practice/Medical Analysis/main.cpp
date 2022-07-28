#include "MedicalAnalysis.h"
#include <iostream>
#include "ui.h"
#include <fstream>

using namespace std;

int main() {
    Person person = Person("test");
    std::string BMIfilename = R"(C:\Users\Aurelian\CLionProjects\Test2practice_seminar\BMI.txt)";
    std::string BPfilename = R"(C:\Users\Aurelian\CLionProjects\Test2practice_seminar\BP.txt)";
    person.addAllAnalysis(BMIfilename, BPfilename);
    UI ui = UI(person);

    ui.run();

    return 0;
}
