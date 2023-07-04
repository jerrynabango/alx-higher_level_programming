#!/usr/bin/python3
"""Max integer - Unittest"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """max integer"""
    def test_mixed_data_types(self):
        """Test float & integers"""
        result = max_integer([-18, -6, 7, -62])
        self.assertEqual(7, result)  #instance of TestCase

    def test_single_list(self):
        """Test for a single element"""
        result = max_integer([23])
        self.assertEqual(23, result)  #instance of TestCase

    def test_sorted_list(self):
        """Test sorted list"""
        result = max_integer([5, 25, 125, 625])
        self.assertEqual(625, result)  #instance of TestCase

    def test_reversed_list(self):
        """Test reversed list"""
        result = max_integer([64, 32, 16, 4])
        self.assertEqual(64, result)  #instance of TestCase

    def test_list(self):
        """Test empty list"""
        result = max_integer([])
        self.assertEqual(None, result)  #instance of TestCase

    def test_floats(self):
        """Test floats"""
        result = max_integer([3.2, 7.5, 1.8, 6.5])
        self.assertEqual(7.5, result)  #instance of TestCase

    def test_string(self):
        """Test strings"""
        names = ['zaki', 'slam', 'Chillz', 'zaki']
        result = max_integer(names)
        self.assertEqual('zaki', result)  #instance of TestCase

    def test_negative_integers(self):
        """Test negative integers"""
        result = max_integer([-34, -36, -7, -11])
        self.assertEqual(-7, result)  #instance of TestCase

    def test_equal_elements(self):
        """Test equal elements"""
        result = max_integer([1, 1, 1, 1])
        self.assertEqual(1, result)  #instance of TestCase

if __name__ == '__main__':
    unittest.main()
