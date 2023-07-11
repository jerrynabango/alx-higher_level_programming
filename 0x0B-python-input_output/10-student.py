#!/usr/bin/python3
""""Student to JSON with filter"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list:
            dictionary = {student: self.__dict__[student]
                     for student in attrs if student in self.__dict__}
            return dictionary
        else:
            return self.__dict__
