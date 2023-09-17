#!/usr/bin/python3
"""
Cities in state
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_city import City


def cities():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for cities_states in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(cities_states[0] + ": (" + str(cities_states[1]) + ") " + cities_states[2])


if __name__ == "__main__":
    cities()
