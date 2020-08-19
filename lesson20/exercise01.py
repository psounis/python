import unittest
from waiter import Waiter, Barista


class WaiterTestCase(unittest.TestCase):
    def setUp(self):
        self.baristaObj = Barista("Bob", 10000)

    def test_init(self):
        w = Waiter("Tom", 5000)
        self.assertEqual(w.full_name, "Tom")
        self.assertEqual(w.salary, 5000)
        self.assertEqual(w.served_cnt, 0)

    def test_serve(self):
        w = Waiter("Tom", 5000)
        w.serve(50, self.baristaObj)
        self.assertEqual(w.served_cnt, 50)
