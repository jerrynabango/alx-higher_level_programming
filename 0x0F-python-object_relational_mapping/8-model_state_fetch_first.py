#!/usr/bin/python3
"""
First state
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def first_state():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print(state.id, state.name, sep=": ")


if __name__ == "__main__":
    first_state()
