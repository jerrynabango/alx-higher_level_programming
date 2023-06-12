#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        tuple_length = (0, None)
        return tuple_length
    else:
        return length, sentence[0:1]