#!/usr/bin/python3
"""
From city
"""

import sys
from relationship_state import State, Base
from sqlalchemy import (create_engine)
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


def From ():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        for from_city in state.cities:
            print(from_city.id, from_city.name, sep=": ", end="")
            print(" -> " + state.name)


if __name__ == "__main__":
    From()
