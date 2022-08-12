# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\CourseExample_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\CourseExample_autogen.dir\\ParseCache.txt"
  "CourseExample_autogen"
  )
endif()
