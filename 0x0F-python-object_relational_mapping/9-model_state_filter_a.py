#!/usr/bin/python3
"""
Contains 'a'
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def contains():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for a in session.query(State).filter(State.name.like('%a%')):
        print(a.id, a.name, sep=": ")


if __name__ == "__main__":
    contains()
