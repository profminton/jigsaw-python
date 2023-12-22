CMAKE_MINIMUM_REQUIRED(VERSION 3.15.7...3.28.1)

IF (NOT SKBUILD)
    MESSGE(FATAL_ERROR "This project is only intended to be built with scikit-build")
ENDIF ()

SET(SKBUILD_PROJECT_NAME "jigsawpy" CACHE STRING "Name of project set by scikit-build")

# Set the project version

PROJECT(${SKBUILD_PROJECT_NAME})

# Use the old method to get Python packages, as that's what scikit-build uses
IF (${CMAKE_VERSION} VERSION_GREATER_EQUAL "3.27")
    CMAKE_POLICY(SET CMP0148 OLD)
ENDIF ()

SET(CMAKE_INSTALL_PREFIX ${SKBUILD_PLATLIB_DIR}/${SKBUILD_PROJECT_NAME})
SET(CMAKE_INSTALL_BINDIR "_bin")
SET(CMAKE_INSTALL_LIBDIR "_lib")
IF (APPLE)
    SET(CMAKE_INSTALL_RPATH "@loader_path/../${CMAKE_INSTALL_LIBDIR}")
ELSEIF (LINUX)
    SET(CMAKE_INSTALL_RPATH "$ORIGIN/../${CMAKE_INSTALL_LIBDIR}")
ENDIF ()

# The following section is modified from Numpy f2py documentation
IF(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
    MESSAGE(FATAL_ERROR "In-source builds not allowed. Please make a new directory (called a build directory) and run CMake from there.\n")
ENDIF()

# Ensure scikit-build modules
FIND_PACKAGE(Python COMPONENTS Interpreter Development.Module NumPy REQUIRED)

ADD_SUBDIRECTORY ("${CMAKE_SOURCE_DIR}/external/jigsaw/src")

# The jigsaw CMakeLists.txt is set up to install binaries to ./bin and libraries to ./lib, so we ned to install them to the correct location
INSTALL(
    DIRECTORY ${CMAKE_SOURCE_DIR}/bin/ 
    DESTINATION ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_BINDIR} 
    USE_SOURCE_PERMISSIONS
)
INSTALL(
    DIRECTORY ${CMAKE_SOURCE_DIR}/lib/ 
    DESTINATION ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR} 
    USE_SOURCE_PERMISSIONS
)
# Make sure the local version of the package gets the binaries and libraries as well as the installed version, otherwise the tests fail
INSTALL(
    DIRECTORY ${CMAKE_SOURCE_DIR}/bin/ 
    DESTINATION ${CMAKE_SOURCE_DIR}/${SKBUILD_PROJECT_NAME}/_bin
    USE_SOURCE_PERMISSIONS
)
INSTALL(
    DIRECTORY ${CMAKE_SOURCE_DIR}/lib/ 
    DESTINATION ${CMAKE_SOURCE_DIR}/${SKBUILD_PROJECT_NAME}/_lib
    USE_SOURCE_PERMISSIONS
)



