cmake_minimum_required(VERSION 3.21)
project(a3_4_913_Iancu_Gheorghe_Aurelian)

set(CMAKE_CXX_STANDARD 14)

add_executable(a3_4_913_Iancu_Gheorghe_Aurelian
        domain.c
        domain.h
        main.c
        repository.c
        repository.h
        service.c
        service.h
        ui.c
        ui.h
        dynamicArray.h
        dynamicArray.c
        undoRedo.c
        undoRedo.h)
