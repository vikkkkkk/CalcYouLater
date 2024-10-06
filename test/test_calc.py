import unittest
from core.calc_core_wrapper import (
    add, subtract, multiply, divide, 
    calculate_infix, calculate_rpn, 
    sin, cos, tan, ctg
)
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertAlmostEqual(add(2, 3), 5)
        self.assertAlmostEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertAlmostEqual(subtract(5, 3), 2)
        self.assertAlmostEqual(subtract(2, 5), -3)

    def test_multiply(self):
        self.assertAlmostEqual(multiply(3, 4), 12)
        self.assertAlmostEqual(multiply(-1, 1), -1)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(30), 0.5)
        self.assertAlmostEqual(sin(90), 1)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(60), 0.5)
        self.assertAlmostEqual(cos(90), 0)

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(45), 1)
        with self.assertRaises(ValueError):
            tan(90)

    def test_ctg(self):
        self.assertAlmostEqual(ctg(45), 1)
        with self.assertRaises(ValueError):
            ctg(0)

    def test_calculate_infix(self):
        self.assertAlmostEqual(calculate_infix("2 + 3", 0), 5)
        self.assertAlmostEqual(calculate_infix("5 * x", 2), 10)
        self.assertAlmostEqual(calculate_infix("sin(90)", 0), 1)  # Убедитесь, что синус в радианах

    def test_calculate_rpn(self):
        self.assertAlmostEqual(calculate_rpn("3 4 +"), 7)
        self.assertAlmostEqual(calculate_rpn("5 1 2 + 4 * + 3 -"), 14)
        with self.assertRaises(ValueError):
            calculate_rpn("5 0 /")

if __name__ == '__main__':
    unittest.main()
