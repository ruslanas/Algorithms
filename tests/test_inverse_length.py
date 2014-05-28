from unittest import TestCase
from inverselen import inverse_length

__author__ = 'Ruslanas Balčiūnas'

class TestInverse_length(TestCase):
    def test_inverse_length(self):
        self.assertEqual(0, inverse_length([1, 2, 3, 4, 5, 6]))
        self.assertEqual(3, inverse_length([1, 3, 5, 2, 4, 6]))
        self.assertEqual(15, inverse_length([6, 5, 4, 3, 2, 1]))
