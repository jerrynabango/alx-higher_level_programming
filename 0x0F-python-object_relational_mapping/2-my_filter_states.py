#!/usr/bin/python3
"""
Filter states by user input
"""

import MySQLdb
import sys


def all_states():
    db = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    all_states()
