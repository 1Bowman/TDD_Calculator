import unittest
import calculator


class TestCalculatorFunctions(unittest.TestCase):

    def test_add_floats(self):
        self.assertEqual(calculator.add(5.0, 1.0), 6.0)

    def test_add_ints(self):
        self.assertEqual(calculator.add(11, 12), 23.0)

    def test_subtract_ints(self):
        self.assertEqual(calculator.sub(6, 5), 1.0)

    def test_subtract_ints_neg(self):
        self.assertEqual(calculator.sub(5, 6), -1.0)

    def test_subtract_floats(self):
        self.assertEqual(calculator.sub(24.1, 12.05), 12.05)

if __name__ == "__main__":
    unittest.main()
