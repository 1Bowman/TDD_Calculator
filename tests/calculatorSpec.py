import unittest
import calculator


class TestCalculatorFunctions(unittest.TestCase):

    def test_add_floats(self):
        self.assertEqual(calculator.add(5.0, 1.0), 6.0)

    def test_add_ints(self):
        self.assertEqual(calculator.add(11, 12), 23.0)


if __name__ == "__main__":
    unittest.main()
