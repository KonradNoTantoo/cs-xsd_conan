cmake_minimum_required(VERSION 2.8.12)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_custom_command (
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.hxx  ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.cxx
  COMMAND xsd cxx-parser --std c++11 --type-map ${CMAKE_CURRENT_SOURCE_DIR}/test_package.map ${CMAKE_CURRENT_SOURCE_DIR}/test_package.xsd
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/test_package.map ${CMAKE_CURRENT_SOURCE_DIR}/test_package.xsd
  )

add_custom_target (CUSTOM_FILE_test_package DEPENDS
  ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.hxx
  ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.cxx)

include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR})

add_executable(${PROJECT_NAME} test_package.cpp ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.cxx)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

add_dependencies(${PROJECT_NAME} CUSTOM_FILE_conan_test)