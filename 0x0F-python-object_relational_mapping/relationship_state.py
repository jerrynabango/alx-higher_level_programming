#!/usr/bin/python3
"""
State
"""

from sqlalchemy import Column,  MetaData, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """
    Defines the state of a state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
