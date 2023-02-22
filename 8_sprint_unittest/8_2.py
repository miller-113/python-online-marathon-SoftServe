import unittest
from unittest import main
"""
You have function divide

Please, write the code with unit tests for the function "divide":
minimum 3 tests
must chek all flows
all test must be pass
no failures
no skip
"""

def divide(num_1, num_2):
    return float(num_1 / num_2)


class DivideTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(divide(6, 3), 2)

    def test_2(self):
        self.assertEqual(divide(100, 5), 20)

    def test_3(self):
        self.assertEqual(divide(77, 7), 11)

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == '__main__':
    # main()
    pass