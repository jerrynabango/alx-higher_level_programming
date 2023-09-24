#!/usr/bin/python3
"""
Get a state
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def get():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    get_state = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(get_state[0].id)
    except IndexError:
        print("Not found")


if __name__ == "__main__":
    get()
