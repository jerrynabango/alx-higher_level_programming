#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    usa = cursor.fetchall()

    for state in usa:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
