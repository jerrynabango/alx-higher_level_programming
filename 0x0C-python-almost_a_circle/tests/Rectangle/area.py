#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.rectangle import Rectangle


class TestMethodRectangleArea(unittest.TestCase):
    @classmethod
    def setUp(self):
        """Setup the test case.""" 
        self.r = Rectangle(7, 2, 1, 5)

    def tearDown(self):
        """Called when the test case is stopped."""
        del self.r

    def test_WithModified_Attributes(self):
        """
        Checks that the attributes are correct for the test case.
        instances: self.r.width, self.r.height
        """
        self.r.width = 10
        self.r.height = 10
        area = self.r.width * self.r.height
        self.assertEqual(area, 100)

    def test_WithValid_HeightAndWidth(self):
        """
        Checks that the height and width of the area are the same
        for both areas and areas with valid height and width values
        and width values are returned respectively
        """
        area = self.r.area()
        self.assertEqual(area, 15)

    def test_With_Argument(self):
        """
        Checks that the height and width values are correct
        and returns them correctly
        """
        with self.assertRaises(TypeError):
            self.r.area(7, 5)


if __name__ == 'main':
    unittest.main()
