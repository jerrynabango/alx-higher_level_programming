#!/usr/bin/python3
"""
from city"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City


def from_city():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city_from in session.query(State).order_by(State.id):
        for city_ins in city_from.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + city_from.name)


if __name__ == "__main__":
    from_city()
