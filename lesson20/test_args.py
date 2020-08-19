import unittest
from args import my_sum  # import function to be tested


class MySumTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(my_sum(1, 2, 3), 6)

    def test_2(self):
        self.assertEqual(my_sum(), 0)
