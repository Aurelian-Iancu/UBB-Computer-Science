#include <iostream>

#include "ShortTest.h"
#include "ExtendedTest.h"

int main(){
    testAll();
    testExtra();
    testAllExtended();
    std::cout<<"Finished IL Tests!"<<std::endl;
	system("pause");
}