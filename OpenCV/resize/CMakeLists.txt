cmake_minimum_required(VERSION 2.8)
project(Resize)

set(Resize_VERSION_MAJOR 1)
set(Resize_VERSION_MINOR_0)

configure_file (
	"${PROJECT_SOURCE_DIR}/ResizeConfig.h.in"
	"${PROJECT_BINARY_DIR}/ResizeConfig.h"
	)

include_directories("${PROJECT_BINARY_DIR}")
#include_directories("${OpenCV_INCLUDE_DIRS}")

find_package(OpenCV 3 REQUIRED)

add_executable(Resize resize.cpp)
target_link_libraries(Resize ${OpenCV_LIBS})

include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
else()
        message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()