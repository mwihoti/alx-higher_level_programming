#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test for max_integer"""

    def test_ordered_list(self):
        """test value in ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([20, 4, 5, 12]), 20)

    def test_string(self):
        """Test in strings"""
        name = "zip"
        self.assertEqual(max_integer(name), 'z')

    def test_floats(self):
        """Test floats"""
        self.assertEqual(max_integer([20.6, 99.9, 60.3, 89.5]),99.9)
