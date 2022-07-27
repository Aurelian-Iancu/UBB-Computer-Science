cmake_minimum_required(VERSION 3.21)
project(SortedIteratedList)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(SortedIteratedList
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        ListIterator.cpp
        ListIterator.h
        ShortTest.cpp
        ShortTest.h
        SortedIteratedList.cpp
        SortedIteratedList.h)
