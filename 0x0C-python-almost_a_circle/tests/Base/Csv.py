#!/usr/bin/python3

"""Test for the base csv file"""
import os
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSaveToCsvFile(unittest.TestCase):
    @classmethod
    def tearDown(self):
        """Called after the save operation"""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_CsvFileContent_And_Length(self):
        """
        Check that the file content and length
        are correct when converting to CSV.
        """
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertTrue("1,2,3,4,5", file.read())

        s = Square(1, 2, 3, 4)
        Square.save_to_file_csv([s])
        with open("Square.csv", encoding='utf-8') as file:
            self.assertTrue("1,2,3,4", file.read())

    def test_CsvFile_Creation(self):
        """Check that the file is created correctly with the correct format"""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        self.assertTrue(os.path.exists("Rectangle.csv"))

        s = Square(1, 2, 3, 4)
        Square.save_to_file_csv([s])
        self.assertTrue(os.path.exists("Square.csv"))

    def test_CsvFile_OverWrite(self):
        """
        Check that the file is written correctly
        when writing to a CSV file"""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        r = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertTrue("6,7,8,9,10", file.read())

    def test_With_None(self):
        """Check that the given string is not empty"""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertEqual("\n", file.read())

    def test_With_NoArguments(self):
        """Check that the argument list is correctly formatted"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_With_ExcessArguments(self):
        """Check that rectangle with arguments is correctly saved to file"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([], [])

    def test_With_AnEmptyList(self):
        """Check that the list contains only a single element"""
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", encoding='utf-8') as file:
            self.assertEqual("\n", file.read())


class TestLoadFromCsvFile(unittest.TestCase):
    @classmethod
    def tearDown(self):
        """Called when the test is stopped"""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_CheckLines_And_LineValues(self):
        """Check that lines and lines values are correctly formatted"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file_csv([r1, r2])
        rects = Rectangle.load_from_file_csv()
        self.assertEqual(str(rects[0]), str(r1))
        self.assertEqual(str(rects[1]), str(r2))
        self.assertTrue(all(type(r) == Rectangle for r in rects))

        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file_csv([s1, s2])
        squares = Square.load_from_file_csv()
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))
        self.assertTrue(all(type(s) == Square for s in squares))

    def test_CsvFileDoesNoExist(self):
        """Check that the file does not exist in the given directory"""
        response = Square.load_from_file_csv()
        self.assertEqual([], response)

    def test_With_ExcessArguments(self):
        """
        Check that the argument count is correct
        when the number of arguments is specified in the constructor
        """
        with self.assertRaises(TypeError):
            Square.load_from_file_csv([], [])


if __name__ == "__main__":
    unittest.main()
