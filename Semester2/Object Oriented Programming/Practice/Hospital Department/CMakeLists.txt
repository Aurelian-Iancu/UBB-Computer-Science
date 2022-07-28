cmake_minimum_required(VERSION 3.21)
project(Test2practice_917)

set(CMAKE_CXX_STANDARD 14)

add_executable(Test2practice_917 main.cpp
        Service.h
        Service.cpp
        UI.h
        UI.cpp
        HospitalDepartment.cpp
        HospitalDepartment.h
        NeonatalUnit.h
        Surgery.cpp
        Surgery.h
        NeonatalUnit.cpp
        Service.cpp)
