cmake_minimum_required(VERSION 3.21)
project(Test915)

set(CMAKE_CXX_STANDARD 14)

add_executable(Test915 main.cpp domain.cpp domain.h service.h service.cpp repository.cpp repository.h ui.cpp ui.h dynamicVector.cpp dynamicVector.h tests.cpp tests.h)
