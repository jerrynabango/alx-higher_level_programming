#!/usr/bin/python3
for alphabet in range(97, 123):
    if (chr(alphabet) == "e" or chr(alphabet) == "q"):
        continue
    print(chr(alphabet).format(alphabet), end="")
