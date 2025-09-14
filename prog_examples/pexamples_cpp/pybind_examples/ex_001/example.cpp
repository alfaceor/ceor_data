#include <pybind11/pybind11.h>

// A simple C++ function
int add(int a, int b) {
    return a + b;
}

// Define a Python module
PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin";  // Optional docstring
    m.def("add", &add, "A function that adds two numbers");
}

