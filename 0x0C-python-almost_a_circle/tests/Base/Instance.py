#!/usr/bin/python3
"""Test Base"""
import unittest
from models.base import Base


class BaseTestInstantiation(unittest.TestCase):
    def test_With_IdNone(self):
        """Check that instantiation works with None values"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_With_ListId(self):
        """Check that the given list id is not NaN"""
        b1 = Base([1, 2])
        self.assertEqual(b1.id, [1, 2])

    def test_With_outId(self):
        """
        Check that the given id is not in
        the database and returns False if it is not
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_With_IntegerId(self):
        """
        Check that the integer id is not the same
        as the integer id passed in the constructor function
        """
        b1 = Base(2)
        self.assertEqual(b1.id, 2)

    def test_With_FloatId(self):
        """
        Check that the integer id passed in
        the constructor function returns a float id
        """
        b1 = Base(5.5)
        self.assertEqual(b1.id, 5.5)

    def test_With_FloatNanId(self):
        """
        Check that the float id is correctly
        initialized with a float id that is not NaN
        """
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_With_ByteId(self):
        """Check that the given byte id is not NaN"""
        self.assertEqual(b'DevOps', Base(b'DevOps').id)

    def test_With_FloatInfId(self):
        """Check that the given float id is not NaN"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_With_ByteId(self):
        """Check that the given byte id is not NaN"""
        self.assertEqual(b'DevOps', Base(b'DevOps').id)

    def test_With_StringId(self):
        """Check that the given string id is not NaN"""
        b1 = Base("Hello")
        self.assertEqual(b1.id, "Hello")

    def test_With_TupleId(self):
        """Check that the tuple id is not NaN"""
        b1 = Base((2, 3))
        self.assertEqual(b1.id, (2, 3))

    def test_With_ExcessArgumenents(self):
        """
        Check that exceptions are raised when trying to
        raise an exception that doesn not exist in the database
        """
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_Acces_To_PrivateAttribute(self):
        """Check that the attribute name is private attribute name"""
        with self.assertRaises(AttributeError):
            b1 = Base(2)
            print(b1.__nb_objects)

    def test_Access_To_PublicAttribute(self):
        """
        Check that access to a public attribute
        is allowed for the given attribute name"""
        b1 = Base(5)
        b1.id = 7
        self.assertEqual(b1.id, 7)


if __name__ == "__main__":
    unittest.main()
