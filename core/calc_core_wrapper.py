import ctypes
import os

lib_path = os.path.join(os.path.dirname(__file__), 'libcalc_core.so')
calc_core = ctypes.CDLL(lib_path)

# описалово аргументов и возвращаемых значений для каждой функции
calc_core.add.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.add.restype = ctypes.c_double

calc_core.subtract.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.subtract.restype = ctypes.c_double

calc_core.multiply.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.multiply.restype = ctypes.c_double

calc_core.divide.argtypes = (ctypes.c_double, ctypes.c_double)
calc_core.divide.restype = ctypes.c_double

calc_core.calculate_infix.argtypes = (ctypes.c_char_p, ctypes.c_double)
calc_core.calculate_infix.restype = ctypes.c_double

calc_core.calculate_rpn.argtypes = (ctypes.c_char_p,)
calc_core.calculate_rpn.restype = ctypes.c_double

# функции для работы с питоном
def add(a, b):
    return calc_core.add(a, b)

def subtract(a, b):
    return calc_core.subtract(a, b)

def multiply(a, b):
    return calc_core.multiply(a, b)

def divide(a, b):
    if b == 0:
        raise ValueError("АХТУНГ: деление на ноль недопустимо, негодник")
    return calc_core.divide(a, b)

def calculate_infix(expression, x_value=0):
    expression_with_value = expression.replace('x', str(x_value))
    result = calc_core.calculate_infix(expression_with_value.encode('utf-8'), x_value)
    if result != result:
        raise ValueError("АХТУНГ: результат вычисления является NaN")
    return result

def calculate_rpn(expression):
    expr_bytes = expression.encode('utf-8')
    result = calc_core.calculate_rpn(expr_bytes)

    if result != result:
        raise ValueError("АХТУНГ: результат вычисления является NaN")

    return result

def sin(value):
    return calculate_infix(f"sin({value})")

def cos(value):
    return calculate_infix(f"cos({value})")

def tan(value):
    return calculate_infix(f"tan({value})")

def ctg(value):
    return calculate_infix(f"1 / tan({value})")

def sqrt(value):
    if value < 0:
        raise ValueError("АХТУНГ: нельзя взять квадратный корень из отрицательного числа.")
    return calculate_infix(f"sqrt({value})")

def log(value):
    if value <= 0:
        raise ValueError("АХТУНГ: логарифм доступен только для положительных чисел.")
    return calculate_infix(f"log({value})")

def percent(value):
    return calculate_infix(f"{value} / 100")

