#!/usr/bin/python3
"""
All states via SQLAlchemy
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def via():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State).order_by(State.id):
        print(states.id, states.name, sep=": ")


if __name__ == "__main__":
    via()
