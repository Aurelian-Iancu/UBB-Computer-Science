cmake_minimum_required(VERSION 3.21)
project(a8_9_913_Iancu_Gheorghe_Aurelian)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(a8_9_913_Iancu_Gheorghe_Aurelian
        main.cpp
        movie.cpp
        movie.h
        repository.cpp
        repository.h
        service.cpp
        service.h
        ui.cpp
        ui.h
        userRepository.cpp
        userRepository.h
        userService.cpp
        userService.h
        validators.cpp
        validators.h
        movies.txt
        CSVrepository.cpp
        CSVrepository.h
        HTMLrepository.cpp
        HTMLrepository.h
        )
