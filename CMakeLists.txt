cmake_minimum_required(VERSION 3.0)
project(sparke_kinematics)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 11)

##### BASE TF #####

set(BASETF_SOURCES
    src/base_transformations.cpp
)

set(BASETF_HEADERS
    include/base_transformations.hpp
)

add_library(base_transformations ${BASETF_SOURCES} ${BASETF_HEADERS})

target_include_directories(base_transformations
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        /usr/include/eigen3
)

set_target_properties(base_transformations PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin
)

add_executable(test_base_transformations src/test_base_transformations.cpp)
target_link_libraries(test_base_transformations base_transformations leg_transformations)
target_include_directories(test_base_transformations
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

##### LEG TF #####

set(LEGTF_SOURCES
    src/leg_transformations.cpp
)

set(LEGTF_HEADERS
    include/leg_transformations.hpp
)

add_library(leg_transformations ${LEGTF_SOURCES} ${LEGTF_HEADERS})

target_include_directories(leg_transformations
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        /usr/include/eigen3
)

set_target_properties(leg_transformations PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin
)

##### SPARKE LEG IK #####

set(LEGIK_SOURCES
    src/sparke_leg_IK.cpp
)

set(LEGIK_HEADERS
    include/sparke_leg_IK.hpp
)

add_library(sparke_leg_IK ${LEGIK_SOURCES} ${LEGIK_HEADERS})

target_include_directories(sparke_leg_IK
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        /usr/include/eigen3
)

target_link_libraries(sparke_leg_IK base_transformations leg_transformations)

set_target_properties(sparke_leg_IK PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin
)

add_executable(test_sparke_leg_IK src/test_sparke_leg_IK.cpp)
target_link_libraries(test_sparke_leg_IK base_transformations sparke_leg_IK)
target_include_directories(test_sparke_leg_IK
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)