#!/usr/bin/python3
"""
python file that contains the class definition of a State
and an instance Base = declarative_base():
"""

from model_state import State, Base
import sys

from sqlalchemy import (create_engine)


def First_state_model():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    First_state_model()
