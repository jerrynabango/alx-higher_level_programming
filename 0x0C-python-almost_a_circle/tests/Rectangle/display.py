#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangleDisplay(unittest.TestCase):
    @classmethod
    def setUp(self):
        """Set up the display object with the given rectangles"""
        self.r = Rectangle(2, 3)

    def tearDown(self):
        """Called when the display object is destroyed"""
        del self.r

    def checkOutput(self, expected):
        """
        Checks the output of the display object against
        the given expected data
        """
        with patch('sys.stdout', new=StringIO()) as fakeOut:
            self.r.display()
            self.assertEqual(fakeOut.getvalue(), expected)

    def test_With_X(self):
        """
        Checks that the function is called with arguments
        and returns a string representation with the function
        arguments and the function arguments as arguments instead
        """
        self.r.x = 1
        expected = " ##\n ##\n ##\n"
        self.checkOutput(expected)

    def test_With_Y(self):
        """
        Checks that the output of the function is correct
        when given arguments instead of arguments
        """
        self.r.y = 2
        expected = "\n\n##\n##\n##\n"
        self.checkOutput(expected)

    def test_With_XandY(self):
        """Checks that the output of the function is correct
        when given the given coordinates and coordinates
        are in the same coordinate space as the input coordinates
        """
        self.r.x = 1
        self.r.y = 2
        expected = "\n\n ##\n ##\n ##\n"
        self.checkOutput(expected)

    def test_Without_XandY(self):
        """
        Checks that the output of the function is correct
        when the function is called without arguments and
        returns a string representation
        """
        expected = "##\n##\n##\n"
        self.checkOutput(expected)


class TestRectangleString(unittest.TestCase):
    def test_With_XandY(self):
        """Checks that the coordinates"""
        r = Rectangle(3, 5, 6, 7)
        expected = "[Rectangle] ({}) 6/7 - 3/5".format(r.id)
        self.assertEqual(str(r), expected)

    def test_Without_XandY(self):
        """
        Checks that the rectangle string is correctly
        formatted correctly.
        """
        r = Rectangle(3, 5)
        expected = "[Rectangle] ({}) 0/0 - 3/5".format(r.id)
        self.assertEqual(str(r), expected)

    def test_With_XandY_and_Id(self):
        """
        Checks that the given object has the given attributes
        and returns them correctly.
        """
        r = Rectangle(3, 5, 6, 7, 8)
        expected = "[Rectangle] (8) 6/7 - 3/5"
        self.assertEqual(str(r), expected)

    def test_With_X(self):
        """
        Checks that rectangles are correctly formatted
        with x and y coordinates
        """
        r = Rectangle(3, 5, 6)
        expected = "[Rectangle] ({}) 6/0 - 3/5".format(r.id)
        self.assertEqual(str(r), expected)


class TestRectangleDictionary(unittest.TestCase):
    def test_Output(self):
        """
        Checks that output is correctly formatted and
        correctly formatted with a dictionary representation.
        """
        r = Rectangle(1, 2, 3, 4, 5)
        expected = {'id': 5, 'x': 3, 'y': 4, 'width': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), expected)

    def test_With_Args(self):
        """
        Checks that the arguments are correct when using
        the provided dictionary as the dictionary argument.
        """
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(4)

    def test_Object_Change(self):
        """
        Checks that the object changes its properties when
        the object changes its properties.
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()
