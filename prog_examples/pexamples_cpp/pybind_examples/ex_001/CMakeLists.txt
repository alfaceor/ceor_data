cmake_minimum_required(VERSION 3.5)
project(example)

find_package(pybind11 REQUIRED)

pybind11_add_module(example example.cpp)

