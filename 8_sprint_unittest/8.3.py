"""Write the function quadratic_equation with arguments a, b ,c that solution
to quadratic equation without a complex solution.

Write unit tests for this function with QuadraticEquationTest class

Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0
"""

import unittest


def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        try:
            return -b / (2 * a)
        except ZeroDivisionError:
            raise ValueError

    x1 = float((-b + discriminant ** 0.5) / (2 * a))
    x2 = float((-b - discriminant ** 0.5) / (2 * a))

    return x1, x2


class QuadraticEquationTest(unittest.TestCase):
    def test_less_then_zero(self):
        self.assertIsNone(quadratic_equation(5, 2, 5))

    def test_greater_then_zero(self):
        self.assertIsNotNone(quadratic_equation(2, 5, 2))

    def test_equal_then_zero(self):
        self.assertEqual(quadratic_equation(2, 0, 0), 0)

    def test_zero_division_error(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 0, 0)



quadratic_equation(2, 0, 0)