cmake_minimum_required(VERSION 3.21)
project(Test2practice_seminar)

set(CMAKE_CXX_STANDARD 14)

add_executable(Test2practice_seminar
        BMI.h
        BMI.cpp
        BP.cpp
        BP.h
        Person.cpp
        Person.h
        MedicalAnalysis.cpp
        MedicalAnalysis.h
        main.cpp
        Utils.cpp
        Utils.h
        UI.h
        UI.cpp)
