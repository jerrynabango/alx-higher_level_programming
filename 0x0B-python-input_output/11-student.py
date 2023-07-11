#!/usr/bin/python3
""""Student to disk and reload"""


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

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for dict_key, dict_value in json.items():
            if dict_key in self.__dict__:
                self.__dict__[dict_key] = dict_value
