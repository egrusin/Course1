import unittest
from main import *


class DrawTest(unittest.TestCase):
    def test_calculate_1(self):
        self.assertEqual(DrawData(defaults_draw).S, 4.05)

    def test_calculate_2(self):
        self.assertEqual(DrawData(defaults_draw).Dw, 8.64)

    def test_calculate_3(self):
        self.assertEqual(DrawData(defaults_draw).d1, 33.5)
