#!/usr/bin/python3

"""Text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after texts(., ? and :)"""
    text_indent = 0
    texts = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while texts < len(text):
        if text_indent == 0:
            if text[texts] == ' ':
                texts += 1
                continue
            else:
                text_indent = 1

        if text_indent == 1:
            if text[texts] == '?' or text[texts] == '.' or text[texts] == ':':
                print(text[texts])
                print()
                text_indent = 0
            else:
                print(text[texts], end="")
        texts += 1
