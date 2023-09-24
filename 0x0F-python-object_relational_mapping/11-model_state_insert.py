#!/usr/bin/python3
"""
Add a new state
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def add():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='Louisiana')
    session.add(state)
    addState = session.query(State).filter_by(name='Louisiana').first()
    print(addState.id)
    session.commit()


if __name__ == "__main__":
    add()
