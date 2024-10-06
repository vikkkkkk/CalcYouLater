import math
from core.calc_core_wrapper import calculate_infix, sqrt, percent, log

class CalculationModel:
    def __init__(self):
        pass

    def evaluate_expression(self, expression, x_value=0):
        try:
            result = calculate_infix(expression, x_value)
            return result
        except Exception as e:
            print(f"АХТУНГ: ошибка вычисления: {e}")
            return None

    def calculate_sin(self, value):
        return math.sin(math.radians(value))

    def calculate_cos(self, value):
        return math.cos(math.radians(value))

    def calculate_tan(self, value):
        return math.tan(math.radians(value))

    def calculate_ctg(self, value):
        if value % 180 == 0:
            raise ValueError("АХТУНГ: ctg не определен для этого значения")
        return 1 / math.tan(math.radians(value))

    def calculate_sqrt(self, value):
        if value < 0:
            raise ValueError("АХТУНГ: нельзя взять квадратный корень из отрицательного числа")
        return sqrt(value)

    def calculate_percent(self, value):
        return percent(value)

    def calculate_log(self, value):
        if value <= 0:
            raise ValueError("АХТУНГ: логарифм доступен только для положительных чисел")
        return log(value)
