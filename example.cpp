#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

void modify_array(py::array_t<double> input_array) {
    py::buffer_info buf_info = input_array.request();
    double *ptr = static_cast<double *>(buf_info.ptr);

    int X = buf_info.shape[0];

    for (int i = 0; i < X; i++) {
        ptr[i] = ptr[i] * 2;
    }

}

PYBIND11_MODULE(example, m) {
    m.def("modify_array", &modify_array, "Function to double the values of a NumPy array");
}
