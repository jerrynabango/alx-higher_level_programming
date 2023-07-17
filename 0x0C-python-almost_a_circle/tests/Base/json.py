#!/usr/bin/python3

"""
A test module for Base json conversion
"""

import os
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestJsonStringFormat(unittest.TestCase):
    def test_With_None(self):
        """Checks that the string representation of a JSON string is correct"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_RectangleType(self):
        """Checks that the rectangle type of a JSON string is correct"""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertIsInstance(Base.to_json_string([r.to_dictionary()]), str)

    def test_With_EmptyList(self):
        """
        Checks that the list is empty when it contains no elements and
        returns a list containing all elements in the list that are not
        present in the list
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_RectangleJsonLength(self):
        """Checks that the rectangle is correctly formatted"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(52, len(Base.to_json_string([r.to_dictionary()])))

    def test_SquareType(self):
        """
        Checks that a square type is correctly
        classified as a square type
        """
        s = Square(1, 2, 3, 4)
        self.assertIsInstance(Base.to_json_string([s.to_dictionary()]), str)

    def test_SquareJsonLength(self):
        """Checks that square json length is correct"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(38, len(Base.to_json_string([s.to_dictionary()])))

    def test_With_MoreArgments(self):
        """
        Checks that the given string contains more
        than one segment in the given string.
        """
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_With_outArguments(self):
        """
        Checks that the given string does not
        contain arguments.
        """
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestSaveToJsonFile(unittest.TestCase):
    def tearDown(self):
        """Called when saving changes to a file"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_SaveNoneValueToJson(self):
        """
        Checks that saveNoneValueToJson returns None
        if the value is not present in the JSON file
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", encoding="utf-8") as file:
            self.assertEqual("[]", file.read())

        Square.save_to_file(None)
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual("[]", file.read())

    def test_JsonFileCreation(self):
        """
        Checks that the json file exists
        and returns True if it exists
        """
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_ValidateJsonContentLength(self):
        """
        Checks that the json content length
        is correct when given a string
        """
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", encoding='utf-8') as file:
            self.assertEqual(52, len(file.read()))

        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual(38, len(file.read()))

    def test_JsonFileOverwrite(self):
        """Checks that the json file is not overwritten"""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", encoding='utf-8') as file:
            self.assertEqual(52, len(file.read()))
        r = Rectangle(11, 22, 33, 44, 55)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", encoding='utf-8') as file:
            self.assertEqual(57, len(file.read()))

        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual(38, len(file.read()))
        s = Square(11, 22, 33, 44)
        Square.save_to_file([s])
        with open("Square.json", encoding='utf-8') as file:
            self.assertEqual(42, len(file.read()))

    def test_SaveEmptyListToJson(self):
        """
        Checks that the save operation works
        correctly when the list is empty
        """
        Square.save_to_file([])
        with open("Square.json", encoding="utf-8") as file:
            self.assertEqual("[]", file.read())

    def test_SaveToJsonWithExcessArguments(self):
        """
        Checks that save method saves correctly
        when argument count exceeds maximum number of arguments
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])

    def test_SaveToJsonWithoutArguments(self):
        """
        Checks that save to json works correctly
        with arguments passed to save method
        """
        with self.assertRaises(TypeError):
            Square.save_to_file()


class TestFromJsonStringToPythonList(unittest.TestCase):
    def test_FromJsonToList(self):
        """
        Check that fromJsonToList works
        correctly with lists of objects
        """
        pyList = [{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]
        jsonString = Rectangle.to_json_string(pyList)
        J2P = Rectangle.from_json_string(jsonString)
        self.assertEqual(J2P, pyList)

        pyList = [{"id": 1, "x": 2, "y": 3, "size": 4}]
        jsonString = Square.to_json_string(pyList)
        J2P = Square.from_json_string(jsonString)
        self.assertEqual(J2P, pyList)

    def test_TypeCheck(self):
        """Check that type checking works correctly in Python lists"""
        pyList = [{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]
        jsonString = Rectangle.to_json_string(pyList)
        J2P = Rectangle.from_json_string(jsonString)
        self.assertEqual(type(J2P), list)

    def test_With_EmptyJsonStringArray(self):
        """
        Check that the json string array
        is correctly initialized properly
        """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_With_NoneArgument(self):
        """Check that the argument is not None when given a None value"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_With_ExcessArguments(self):
        """
        Check that exceptions are raised when trying
        to access a method that does not exist
        """
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])

    def test_With_NoArgument(self):
        """
        Check that the argument is not empty
        when provided with a json string
        """
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestLoadFromJsonFile(unittest.TestCase):

    @classmethod
    def tearDown(self):
        """Called when loading from a file"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_CheckLinesAndLineValues(self):
        """Check that lines and lines values are correctly formatted"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 6, 7, 8, 9)
        Rectangle.save_to_file([r1, r2])
        rects = Rectangle.load_from_file()
        self.assertEqual(str(rects[0]), str(r1))
        self.assertEqual(str(rects[1]), str(r2))
        self.assertTrue(all(type(r) == Rectangle for r in rects))

        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))
        self.assertTrue(all(type(s) == Square for s in squares))

    def test_With_ExessArguments(self):
        """Check that the json file does not exist with arguments"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], [])

    def test_JsonFileDoesNotExist(self):
        """Check that the json file does not exist"""
        response = Square.load_from_file()
        self.assertEqual(response, [])


if __name__ == "__main__":
    unittest.main()
