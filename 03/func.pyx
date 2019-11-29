#declare c-style function by cdef argument
# except? -2: usually followed after function declaration.
# except? -2: means an error will be checked for if -2 is returned
# Warning: using cdef to declare function causes that python can't call it again.
# if you use cpdef keyword, that will create a python wrapper

cpdef double f(double x) except? -2:
    return x ** 2 - x



def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx

