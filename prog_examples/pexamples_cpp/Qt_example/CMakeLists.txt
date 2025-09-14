cmake_minimum_required(VERSION 3.10)

project(CalculatorApp LANGUAGES CXX)

find_package(Qt6 COMPONENTS Core Gui Widgets REQUIRED)

add_executable(calculator_app calculator.cpp)

target_link_libraries(calculator_app PRIVATE Qt6::Core Qt6::Gui Qt6::Widgets)

