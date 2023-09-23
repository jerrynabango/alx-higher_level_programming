#!/usr/bin/python3
"""
Get all states
"""

import sys
import MySQLdb


def state():
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    items = cursor.fetchall()

    for item in items:
        print(item)
    cursor.close()
    db.close()


if __name__ == "__main__":
    state()
