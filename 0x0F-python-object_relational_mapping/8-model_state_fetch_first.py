#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def state_object():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    object = session.query(State).first()

    if object is None:
        print("Nothing")
    else:
        print(object.id, object.name, sep=": ")


if __name__ == "__main__":
    state_object()
