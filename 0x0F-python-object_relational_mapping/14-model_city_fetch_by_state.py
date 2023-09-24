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

    for cit_state in (session.query(State.name, City.id, City.name)
                      .filter(State.id == City.state_id)):
        print(cit_state[0] + ": (" + str(cit_state[1]) + ") " + cit_state[2])


if __name__ == "__main__":
    cities()
