#!/usr/bin/python3
"""
script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

def state_a():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for all_state in session.query(State).filter(State.name.like('%a%')):
        print(all_state.id, all_state.name, sep=": ")


if __name__ == '__main__':
    state_a()
