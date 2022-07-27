cmake_minimum_required(VERSION 3.21)
project(a5_6_913_Iancu_Gheorghe_Aurelian)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(a5_6_913_Iancu_Gheorghe_Aurelian
        movie.cpp
        movie.h
        dynamicVector.cpp
        dynamicVector.h
        service.h
        service.cpp
        repository.h
        repository.cpp
        ui.cpp
        ui.h
        main.cpp tests.h tests.cpp userRepository.cpp userRepository.h userService.cpp userService.h
        comparator.cpp
        comparator.h)