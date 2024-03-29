import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_power(self):
        result = rpn.calculate("3 3 ^")
        self.assertEqual(27, result)
    def test_in(self):
        result = rpn.calculate("4 4 @")
        self.assertEqual(1, result)
    def test_in2(self):
        result = rpn.calculate("4 5 @")
        self.assertEqual(0, result)

if(__name__ == '__main__'):
    unittest.main()
