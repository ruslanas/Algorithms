from unittest import TestCase
from msort import merge_sort

__author__ = 'Ruslanas Balčiūnas'

class TestMerge_sort(TestCase):
    def test_merge_sort(self):
        self.assertEqual([1, 2, 3, 4, 6, 6], merge_sort([2, 4, 6, 6, 1, 3]), 'Sort failed')
        self.assertEqual([1, 1, 2, 2], merge_sort([2, 1, 2, 1]), 'Sort failed')
        self.assertEqual([1, 2, 3, 4, 5], merge_sort([2, 1, 4, 3, 5]), 'Odd length sort failed')
        self.assertEqual(['a', 'b', 'c'], merge_sort(['b', 'a', 'c']), 'Letter sorting failed')
        self.assertEqual(['abc', 'acb', 'adb'], merge_sort(['adb', 'abc', 'acb']), 'String sorting failed')
