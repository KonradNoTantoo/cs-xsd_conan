cmake_minimum_required(VERSION 3.3)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_custom_target (CUSTOM_FILE_test_package DEPENDS
	${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.hxx
	${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.cxx)

include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR})

add_executable(${PROJECT_NAME} test_package.cpp ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.cxx)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

add_dependencies(${PROJECT_NAME} CUSTOM_FILE_test_package)

# Try to detect if compiler is C++11 aware
if(cxx_auto_type IN_LIST CMAKE_CXX_COMPILE_FEATURES)
	set(XSD_CXX_OPTIONS "--std" "c++11")

	set_target_properties(${PROJECT_NAME} PROPERTIES
		CXX_STANDARD 11
		CXX_STANDARD_REQUIRED YES
		CXX_EXTENSIONS NO
	)
else()
	set(XSD_CXX_OPTIONS "")
endif()

add_custom_command (
	OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.hxx  ${CMAKE_CURRENT_BINARY_DIR}/test_package-pskel.cxx
	COMMAND cs-xsd cxx-parser ${XSD_CXX_OPTIONS} --type-map ${CMAKE_CURRENT_SOURCE_DIR}/test_package.map ${CMAKE_CURRENT_SOURCE_DIR}/test_package.xsd
	DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/test_package.map ${CMAKE_CURRENT_SOURCE_DIR}/test_package.xsd
	)