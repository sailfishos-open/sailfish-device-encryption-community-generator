cmake_minimum_required(VERSION 3.5)

project(sailfish-device-encryption-community-generator
    LANGUAGES CXX
    VERSION 0.1
    DESCRIPTION "SystemD Generator for Device Encryption"
    )

find_package (Qt5 COMPONENTS Core REQUIRED)

include(FindPkgConfig)

set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# sources

## C++ sources
file(GLOB CXX_SRC src/*.cpp)
file(GLOB CXX_HEADERS src/*.h)

add_custom_target(Sources SOURCES
    ${QML_SRC}
    ${CXX_SRC} ${CXX_HEADERS}
    rpm/generator.spec
    )

# compilation
add_executable(sailfish-device-encryption-community-generator ${CXX_SRC} ${CXX_HEADERS})

target_compile_definitions(sailfish-device-encryption-community-generator PRIVATE
    $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>
    )
target_include_directories(sailfish-device-encryption-community-generator PRIVATE
    $<BUILD_INTERFACE:
    >)
target_link_libraries(sailfish-device-encryption-community-generator
    Qt5::Core
    sfosdevenc
    )

# install from RPM SPEC
