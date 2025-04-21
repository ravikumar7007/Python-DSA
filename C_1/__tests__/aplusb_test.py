import unittest
from C_1.aplusb import sumOfTwoNumbers


class TestSumOfTwoNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sumOfTwoNumbers(3, 5), 8)

    def test_negative_numbers(self):
        self.assertEqual(sumOfTwoNumbers(-3, -5), -8)

    def test_mixed_sign_numbers(self):
        self.assertEqual(sumOfTwoNumbers(-3, 5), 2)

    def test_zero_and_number(self):
        self.assertEqual(sumOfTwoNumbers(0, 5), 5)
        self.assertEqual(sumOfTwoNumbers(5, 0), 5)

    def test_large_numbers(self):
        self.assertEqual(sumOfTwoNumbers(1000000, 2000000), 3000000)


if __name__ == "__main__":
    unittest.main()
