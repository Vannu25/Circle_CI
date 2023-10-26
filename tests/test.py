import unittest
from tests import main


class test1(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = main.do_stuff_add(num)
        self.assertEqual(result, 15)

