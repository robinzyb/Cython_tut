from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello world app',
        ext_modules=cythonize(["primes.pyx", 'primes_py.py'], annotate=True))
