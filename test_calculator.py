"""Three fixed tests for the public synthetic development trial."""

import unittest

from calculator import add


class CalculatorTests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(4, 7), 11)

    def test_negative(self):
        self.assertEqual(add(-3, 2), -1)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
