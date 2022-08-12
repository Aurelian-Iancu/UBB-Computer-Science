cmake_minimum_required(VERSION 3.21)
project(Test914)

set(CMAKE_CXX_STANDARD 14)

add_executable(Test914 main.cpp dynamicVector.cpp dynamicVector.h domain.cpp domain.h tests.cpp tests.h service.cpp service.h ui.cpp ui.h repository.cpp repository.h)
