#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def add_new():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    adding_new = State(name='Louisiana')
    session.adding_new(adding_new)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)

    session.commit()


if __name__ == "__main__":
    add_new()
