#!/usr/bin/python3
"""
Delete states
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def delete():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for delete_state in session.query(State).filter(State.name.like('%a%')):
        session.delete(delete_state)
    session.commit()


if __name__ == "__main__":
    delete()
