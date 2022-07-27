# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\a14-913-Iancu-Gheorghe-Aurelian_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\a14-913-Iancu-Gheorghe-Aurelian_autogen.dir\\ParseCache.txt"
  "a14-913-Iancu-Gheorghe-Aurelian_autogen"
  )
endif()
