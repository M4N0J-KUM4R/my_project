# test_main.py

import unittest
from main import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
