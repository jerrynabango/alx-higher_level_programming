#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleUpdateMethod(unittest.TestCase):
    def test_With_OneArgs(self):
        """Checks that the given arguments are correct for the given function"""
        r = Rectangle(1, 1)
        r.update(2)
        self.assertEqual(r.id, 2)

    def test_With_TwoArgs(self):
        """
        Checks that the two arguments are equal
        when using with two arguments instead of one.
        """
        r = Rectangle(1, 1)
        r.update(2, 3)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)

    def test_With_Three_Args(self):
        """
        Checks that the three arguments are the same
        for the three arguments passed to the constructor
        function
        """
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 3, 4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_With_FourArgs(self):
        """Checks that the given arguments are correct for the given image type."""
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def test_With_FiveArgs(self):
        """
        Checks that the given arguments are the same
        size and return the same result
        """
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_With_AboveFiveArgs(self):
        """"
        hecks that the argument is within the range of the argument
        list and returns True if it is within the range  of the argument
        list and False otherwise
        """
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6, 7)
        self.assertEqual("[Rectangle] (2) 5/6 - 3/4", str(r))

    def test_Without_Args(self):
        """
        Checks that the arguments are correct when using
        the provided function with arguments that are not
        specified in the function signature
        """
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def test_With_IdNone(self):
        """Checks rectangle update method with given id."""
        r = Rectangle(1, 1)
        r.update(None)
        self.assertEqual("[Rectangle] ({}) 0/0 - 1/1".format(r.id), str(r))

    def test_With_IdNone_And_MoreArgs(self):
        """Checks that the given arguments are not None and more than one argument"""
        r = Rectangle(1, 1)
        r.update(None, 3, 4, 5)
        self.assertEqual("[Rectangle] ({}) 5/0 - 3/4".format(r.id), str(r))

    def test_With_AboveFiveArgs(self):
        """"
        hecks that the argument is within the range of the argument
        list and returns True if it is within the range  of the argument
        list and False otherwise
        """
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6, 7)
        self.assertEqual("[Rectangle] (2) 5/6 - 3/4", str(r))

    def test_With_InvalidWidth(self):
        """Checks that the given rectangle is invalid width"""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(2, "")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, 0)
            r.update(2, -1)

    def test_With_InvalidHeight(self):
        """Checks that the height is invalid."""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(2, 3, "")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(2, 3, 0)
            r.update(2, 3, -1)

    def test_With_InvalidX(self):
        """Checks that the given value is not a valid"""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 3, 4, "")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(2, 3, 4, -1)

    def test_With_InvalidY(self):
        """Checks that the given value is not a valid number."""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(2, 3, 4, 5, "")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(2, 3, 4, 5, -1)

    def test_Invalid_Width_And_Height(self):
        """Checks that the given value is not a valid value"""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(2, "", 4, -1)

    def test_Invalid_Height_And_X(self):
        """Checks that the height and width of a given object is correct"""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(2, 3, "", -1)

    def test_InvalidXandY(self):
        """
        Checks that the given value is not a number
        and returns False if it is not possible to convert it to a number.
        """
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 3, 4, "", "")

    def test_With_OneKwargs(self):
        """
        Checks that the given keyword argument
        is a string and returns a string representation
        """
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2)
        self.assertEqual(r.id, 2)

    def test_With_TwoKwargs(self):
        """
        Checks that the two arguments are the same
        when using with a single kwarg tuple
        """
        r = Rectangle(1, 1, 1, 1)
        r.update(id=2, width=3)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)

    def test_With_ThreeKwargs(self):
        """
        Checks that the three arguments are the same
        size and returns the same result as expected
        """
        r = Rectangle(1, 1, 1, 1)
        r.update(id=2, width=3, height=4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_With_FourKwargs(self):
        """
        Checks that the given width and height are the same
        size and have the same number of elements in the given
        array.
        """
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2, width=3, height=4, x=5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def test_With_FiveKwargs(self):
        """
        Checks that the given arguments are correct
        for the given parameters and returns a tuple containing the result and the expected result
        """
        r = Rectangle(1, 1, 1, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_With_outKwargsOrder(self):
        """Checks that the given arguments are correct for the given arguments order"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(x=2, height=3, id=4, y=5, width=6)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 5)

    def test_With_KwargsIdAsNone(self):
        """
        Checks that the kwargs argument is provided
        correctly when provided with None as None value
        """
        r = Rectangle(1, 2, 2, 1)
        r.update(id=None)
        self.assertEqual("[Rectangle] ({}) 2/1 - 1/2".format(r.id), str(r))

    def test_With_KwargsIdAsNoneAndMore(self):
        """
        Checks that the given kwargs is not None
        and more than one argument is given as None
        and False otherwise
        """
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(x=2, height=3, id=None, y=5, width=6)
        self.assertEqual("[Rectangle] ({}) 2/5 - 6/3".format(r.id), str(r))

    def test_With_NonEmptyArgsAndKwargs(self):
        """Checks that the arguments passed to the constructor are not empty"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 3, id=4, width=5, height=6, x=7, y=8)
        self.assertEqual("[Rectangle] (2) 1/1 - 3/1", str(r))

    def test_With_InvalidKeyInKwargs(self):
        """
        Checks that the given key is invalid in the given
        kwargs and returns True if it matches the given kwargs
        """
        r = Rectangle(1, 1, 1, 1)
        r.update(z=9, id=2, i=11)
        self.assertEqual(r.id, 2)
        with self.assertRaises(AttributeError):
            z = r.z
            i = r.i

    def test_With_InvalidWidth(self):
        """Checks that the attribute value is correct for a given width value"""
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
            r.update(width=-1)

    def test_With_InvalidHeight(self):
        """Checks that the height using invalid height value"""
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="")

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
            r.update(height=-1)

    def test_With_InvalidX(self):
        """Checks that the value of the given value is not a valid value"""
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-1)

    def test_With_InvalidY(self):
        """Checks that the value passed to the constructor throws an exception"""
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-1)
