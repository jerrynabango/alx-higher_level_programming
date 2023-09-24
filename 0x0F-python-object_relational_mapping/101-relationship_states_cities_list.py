#!/usr/bin/python3
"""
List relationship
"""

from relationship_state import State, Base
from sqlalchemy import (create_engine)
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import sys


def list():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for list_rltnshp in session.query(State).order_by(State.id):
        print(list_rltnshp.id, list_rltnshp.name, sep=": ")

        for lists in list_rltnshp.cities:
            print("    ", end="")
            print(lists.id, lists.name, sep=": ")


if __name__ == "__main__":
    list()
