# path is relative from current directory, if you want to discover the path, use the aliases argument of the cythonize() function.

cdef extern from "Rectangle.cpp":
    pass

# Declare the class with cdef
cdef extern from "Rectangle.h" namespace "shapes":
    cdef cppclass Rectangle:
        # except + if for constructor
        Rectangle() except +
        Rectangle(int, int, int, int) except +
        int x0, y0, x1, y1
        int getArea()
        void getSize(int* width, int* height)
        void move(int, int)
