#!/usr/bin/python3
"""
Cities in state
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_city import City


def City_relationship():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    cit = City(name='San Francisco')
    state.cities.append(cit)

    session.add(state)
    session.add(cit)
    session.commit()


if __name__ == '__main__':
    City_relationship()
