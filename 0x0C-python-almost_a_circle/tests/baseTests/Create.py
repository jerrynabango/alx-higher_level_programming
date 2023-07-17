#!/usr/bin/python3
"""Test Base"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestBaseCreateMethod(unittest.TestCase):

    def test_Create_New_Rectangle_Object(self):
        """Checks that create new rectangle object is created correctly"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        rD1 = r1.to_dictionary()
        r2 = Rectangle.create(**rD1)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_Create_New_Square_Object(self):
        """
        Checks  that the new square object is created correctly
        when creating a new square object with the same name
        and properties as the old square object and properties
        are identical to those of the old square object
        """
        s1 = Square(1, 2, 3, 4)
        sD1 = s1.to_dictionary()
        s2 = Square.create(**sD1)
        self.assertEqual("[Square] (4) 2/3 - 1", str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
