import unittest
import calculator


class TestAddFunctions(unittest.TestCase):

    def test_add_floats(self):
        self.assertEqual(calculator.add(5.0, 1.0), 6.0)

    def test_add_ints(self):
        self.assertEqual(calculator.add(11, 12), 23.0)


class TestSubFunctions(unittest.TestCase):

    def test_subtract_ints(self):
        self.assertEqual(calculator.sub(6, 5), 1.0)

    def test_subtract_ints_neg(self):
        self.assertEqual(calculator.sub(5, 6), -1.0)

    def test_subtract_floats(self):
        self.assertEqual(calculator.sub(24.1, 12.05), 12.05)


class TestMulFunctions(unittest.TestCase):

    def test_mul_floats(self):
        self.assertEqual(calculator.mul(1.0, 10.0), 10.0)

    def test_mul_ints(self):
        self.assertEqual(calculator.mul(15, 10), 150.0)

    def test_mul_negatives(self):
        self.assertEqual(calculator.mul(-1, 12), -12.0)


class TestDivFunctions(unittest.TestCase):

    def test_div_floats(self):
        self.assertEqual(calculator.div(100.0, 10.0), 10.0)

    def test_div_ints(self):
        self.assertEqual(calculator.div(15, 10), 1.5)

    def test_div_negatives(self):
        self.assertEqual(calculator.div(-1, 10), -.1)


if __name__ == "__main__":
    unittest.main()

