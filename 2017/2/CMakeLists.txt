project(aoc2017-12-02 CXX)

add_executable(${PROJECT_NAME} main.cxx)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -g")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # Include Conan-generated file
conan_basic_setup(TARGETS) # Introduce Conan-generated targets

target_link_libraries(${PROJECT_NAME} CONAN_PKG::range-v3)
