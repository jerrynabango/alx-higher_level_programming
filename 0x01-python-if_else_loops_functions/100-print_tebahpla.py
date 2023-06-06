#!/usr/bin/python3
for alpha_reverse in range(26):
    if alpha_reverse % 2 == 0:
        print("{:c}".format(122-alpha_reverse), end = "")
    else:
        print("{:c}".format(90-alpha_reverse), end = "")