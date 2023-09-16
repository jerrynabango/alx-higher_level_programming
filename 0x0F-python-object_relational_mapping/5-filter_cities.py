#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def by_state():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         )

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    usa = cursor.fetchall()

    tmp = list(state[0] for state in usa)
    print(*tmp, sep=", ")

    cursor.close()
    db.close()

if __name__ == "__main__":
    by_state()
