#!/usr/bin/python3
"""
All cities by state
"""

import sys
import MySQLdb


def all():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    states = cursor.fetchall()
    tmp = list(state[0]
               for state in states)
    print(*tmp, sep=", ")
    cursor.close()
    db.close()


if __name__ == "__main__":
    all()
