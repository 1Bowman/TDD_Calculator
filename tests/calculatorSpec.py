import unittest
import calculator


class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        calc = calculator.calc()
        self.assertEqual(calc, 'Hello World')


if __name__ == "__main__":
    unittest.main()
