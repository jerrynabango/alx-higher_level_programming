#!/usr/bin/python3
"""
City
"""

from relationship_state import Base
from sqlalchemy import Column,  MetaData, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class City(Base):
    """
    Defines the city that will be created
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
