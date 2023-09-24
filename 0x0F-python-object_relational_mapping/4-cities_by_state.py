#!/usr/bin/python3
"""
Cities by states
"""

import sys
import MySQLdb


def cit_states():
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    cit_states()
