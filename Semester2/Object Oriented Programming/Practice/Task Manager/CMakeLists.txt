cmake_minimum_required(VERSION 3.21)
project(Test917)

set(CMAKE_CXX_STANDARD 14)

add_executable(Test917 main.cpp dynamicVector.cpp dynamicVector.h repository.cpp repository.h service.cpp service.h ui.cpp ui.h tests.h tests.cpp domain.cpp domain.h)
