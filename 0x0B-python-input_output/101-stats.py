#!/usr/bin/python3
"""Log parsing"""
import sys


"""Number of lines by status code"""
Statuscode = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
total_file_size = 0
log_parse = 0
line = sys.stdin.readline()

while line:
    metrics = line.split()
    if len(metrics) >= 2:
        script_read = log_parse
        if metrics[-2] in Statuscode:
            Statuscode[metrics[-2]] += 1
            log_parse += 1
        try:
            total_file_size += int(metrics[-1])
            if script_read == log_parse:
                log_parse += 1
        except FileNotFoundError:
            if script_read == log_parse:
                line = sys.stdin.readline()
                continue

    if log_parse % 10 == 0:
        print("File size: {:d}".format(total_file_size))
        for key, value in sorted(Statuscode.items()):
            if value:
                print("{:s}: {:d}".format(key, value))
    line = sys.stdin.readline()

print("File size: {:d}".format(total_file_size))
for key, value in sorted(Statuscode.items()):
    if value:
        print("{:s}: {:d}".format(key, value))
