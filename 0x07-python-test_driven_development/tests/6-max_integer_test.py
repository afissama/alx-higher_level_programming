#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class test for Max_Integer function"""

    def test_only_positive(self):
        """ Test for positives values """
        current = max_integer([1, 24, 5, 8, 89])
        expected = 89
        self.assertEqual(current, expected)

    def test_only_negative(self):
        """ Test for negative values """
        current = max_integer([-1, -24, -5, -8, -89])
        expected = -1
        self.assertEqual(current, expected)

    def test_none(self):
        """ Test for empty array """
        current = max_integer([])
        expected = None
        self.assertEqual(current, expected)

    def test_one(self):
        """ Test for empty array """
        current = max_integer([5])
        expected = 5
        self.assertEqual(current, expected)

    def test_middle(self):
        """ Test for empty array """
        current = max_integer([5, 15, 3])
        expected = 15
        self.assertEqual(current, expected)
