#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    def testGetters(self):
        """
        Checks that instant construction works
        correctly with a given rectangle object
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def testSetters(self):
        """
        Checks that the setters function works correctly
        with the given setter function arguments and returns
        a tuple containing the result of the sette
        """
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        self.assertEqual(r.width, 6)
        r.height = 7
        self.assertEqual(r.height, 7)
        r.x = 8
        self.assertEqual(r.x, 8)
        r.y = 9
        self.assertEqual(r.y, 9)

    def test_Rectangle_Is_Base_Instance(self):
        """
        Checks whether a rectangle is a base instance
        of a rectangle with a specified dimensions
        and returns a rectangle instance
        """
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_Instantiate_With_ParamsA(self):
        """
        Checks that instant instantiation of a rectangle
        with a specified dimensions and returns a
        rectangle instance
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id + 1, r2.id)

    def test_Instantiate_With_ParamsB(self):
        """
        Checks instant instantiation with parameters
        and returns the result of the instant
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id + 1, r2.id)

    def test_Instantiate_With_ParamsC(self):
        """Checks that instantiate function works correctly with parameters"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id + 1, r2.id)

    def test_Instantiate_With_FiveParams(self):
        """
        Checks that instant instantiate with five parameters
        works correctly with a single parameter
        """
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_Instantiate_With_ExcessParams(self):
        """
        Checks that instantiate with a excess parameter
        works correctly with instant
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_Instantiate_With_OneParam(self):
        """Checks that instantiation with one parameter works correctly."""
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_Instantiate_WithoutParams(self):
        """
        Checks that instant instantiation
        without parameters works correctly.
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_PrivateAccessRaises(self):
        """Checks that private access"""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            r.__height, r.__width, r.__height, r.__y, r.__x


if __name__ == '__main__':
    unittest.main()
