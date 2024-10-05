import ctypes
import os

lib_path = os.path.join(os.path.dirname(__file__), 'libcalc_core.so')
calc_core = ctypes.CDLL(lib_path)

calc_core.add.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.add.restype = ctypes.c_double

calc_core.subtract.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.subtract.restype = ctypes.c_double

calc_core.multiply.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.multiply.restype = ctypes.c_double

calc_core.divide.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.divide.restype = ctypes.c_double

def add(a, b):
    return calc_core.add(a, b)

def subtract(a, b):
    return calc_core.subtract(a, b)

def multiply(a, b):
    return calc_core.multiply(a, b)

def divide(a, b):
    """НЕ РОБИТ((("""
    if b == 0:
        raise ValueError("АХТУНГ: деление на ноль недопустимо, негодник")
    return calc_core.divide(a, b)
