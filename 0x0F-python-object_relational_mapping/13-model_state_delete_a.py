#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def delete_states():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for deleted_state in session.query(State).filter(State.name.like('%a%')):
        session.delete(deleted_state)

    session.commit()


if __name__ == "__main__":
    delete_states()
