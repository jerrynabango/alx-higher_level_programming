#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleWidth(unittest.TestCase):
    def test_Invalid_Width_Type(self):
        """Checks that the rectangle width is correct for a given width type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            """width should be a 'nan'"""
            Rectangle(float('nan'), 8)

            """width should be a string"""
            Rectangle("Tests", 8)

            """width should be a List"""
            Rectangle([3, 4], 8)

            """width should be a tuple"""
            Rectangle((1,), 8)

            """width should be a dictionary"""
            Rectangle({'a': 1}, 8)

            """width should be infinite float"""
            Rectangle(float('inf'), 8)

            """width should be a float"""
            Rectangle(7.1, 9)

            """width should be a set"""
            Rectangle({3, 2}, 8)

            """width should be None"""
            Rectangle(None, 5)

            """width should be a set"""
            Rectangle(True, 7)

            """width should be a bytes"""
            Rectangle(b'tests', 7)

    def test_With_Zero_Height_Value(self):
        """
        Checks that the rectangle with zero height
        works correctly with the given value of height and width values
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(21, 0)

    def test_With_Zero_Width_Value(self):
        """
        Checks that the value of the given rectangle
        is equal to the given value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 8)

    def test_With_Negative_Height_Value(self):
        """
        Checks that the height value is not negative
        and returns a rectangle with the given height value
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, -6)

    def test_With_Negative_Width_Value(self):
        """
        Checks that the rectangle with a negative
        width value is correctly calculated
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 7)


class TestRectangleHeight(unittest.TestCase):
    def testInvalidWidthType(self):
        """Checks that the given width type is invalid"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            """The height is zero"""
            Rectangle(5, 0)

            """The height is negative"""
            Rectangle(7, -3)

    def test_Invalid_HeightType(self):
        """
        Checks that the height of a rectangle is
        correct for a given height type.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            """height should be a list"""
            Rectangle(7, [12, 7])

            """height should be a float"""
            Rectangle(2, 21.6)

            """height should be infinite float"""
            Rectangle(4, float('inf'))

            """height should be a string"""
            Rectangle("Tests", 1)

            """height should be 'nan'"""
            Rectangle(6, float('nan'))

            """height should be None"""
            Rectangle(7, None)

            """height should be a byte"""
            Rectangle(18, b'tests')

            """height should be a tuple"""
            Rectangle(7, (3,))

            """height should be a dictionary"""
            Rectangle(9, {'a': 4})

            """height should be a boolean"""
            Rectangle(43, True)

            """height should be a set"""
            Rectangle(6, {9, 8})


class TestRectangleX(unittest.TestCase):
    def test_Invalid_XValue(self):
        """Checks that the value of the rectangle is invalid"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            """The x is equal to negative"""
            Rectangle(7, 4, -3)

    def test_Invalid_XType(self):
        """
        Checks that the rectangle is invalid when
        given a value of None and returns None
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            """x should be a list"""
            Rectangle(1, 7, [5, 9])

            """x should be a infinite float"""
            Rectangle(9, 3, float('inf'))

            """x should be a float"""
            Rectangle(2, 7, 31.8)

            """x should be a bytes """
            Rectangle(3, 5, b'tests')

            """x should be 'nan'"""
            Rectangle(4, 1, float('nan'))

            """x should be None"""
            Rectangle(7, 3, None)

            """x should be a set"""
            Rectangle(8, 9, True)

            """x should be a string"""
            Rectangle(7, 6, "Tests")

            """x should be a tuple"""
            Rectangle(1, 7, (9,))

            """x should be a dictionary"""
            Rectangle(8, 4, {'a': 1})

            """x should be a set """
            Rectangle(8, 4, {5, 2})


class TestRectangleY(unittest.TestCase):
    def test_Invalid_YValue(self):
        """Checks that the value of the rectangle is invalid"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            """The y is equal to negative """
            Rectangle(7, 1, 25, -3)

    def test_Invalid_YType(self):
        """
        Checks that the rectangle is invalid when specified
        with invalid YType
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            """ y should be a list """
            Rectangle(7, 1, 25, [7, 25])

            """ y should be a float """
            Rectangle(7, 1, 25, 25.25)

            """ y should be bytes """
            Rectangle(7, 1, 25, b'tests')

            """ y should be a infinite float """
            Rectangle(7, 1, 25, float('inf'))

            """ y should be 'nan' """
            Rectangle(7, 1, 25, float('nan'))

            """ y should be None """
            Rectangle(7, 1, 25, None)

            """ y should be a string """
            Rectangle(7, 1, 25, "tests")

            """ y should be a set """
            Rectangle(7, 1, 25, True)

            """ y should be a set """
            Rectangle(7, 1, 25, {1, 2})

            """ y should be a dictionary """
            Rectangle(7, 1, 25, {'a': 1})

            """ y should be a tuple """
            Rectangle(7, 1, 25, (1,))

            """ y should be a string """
            Rectangle(7, 1, 25, "tests")


if __name__ == "__main__":
    unittest.main()
