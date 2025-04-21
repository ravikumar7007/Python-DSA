import unittest
from C_1.aplusb import sumOfTwoNumbers

class TestSumOfTwoNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sumOfTwoNumbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(sumOfTwoNumbers(-2, -3), -5)

    def test_mixed_sign_numbers(self):
        self.assertEqual(sumOfTwoNumbers(-2, 3), 1)

    def test_zero(self):
        self.assertEqual(sumOfTwoNumbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()