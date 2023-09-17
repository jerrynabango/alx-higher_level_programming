#!/usr/bin/python3
"""
city relationship
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City


def city_relationship():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for citship in session.query(State).order_by(State.id):
        print(citship.id, citship.name, sep=": ")

        for city_ins in citship.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")


if __name__ == "__main__":
    city_relationship()
