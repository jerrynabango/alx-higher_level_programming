#!/usr/bin/python3
"""
SQL Injection
"""

import MySQLdb
import sys


def SQL_Injection():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    cursor = db.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    usa = cursor.fetchall()

    for state in usa:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    SQL_Injection()
