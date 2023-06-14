#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                    'M': 1000}
    roman = [roman_number[x] for x in roman_string] + [0]
    integer = 0

    for roman_numeral in range(len(roman) - 1):
        if roman[roman_numeral] >= roman[roman_numeral+1]:
            integer += roman[roman_numeral]
        else:
            integer -= roman[roman_numeral]

    return integer
