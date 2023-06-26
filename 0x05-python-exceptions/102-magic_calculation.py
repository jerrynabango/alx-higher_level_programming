#!/usr/bin/python3
def magic_calculation(a, b):
    byte = 0
    for code in range(1, 3):
        try:
            if code > a:
                raise Exception('Too far')
            byte += a ** b / code
        except Exception:
            byte = b + a
            break
    return byte
