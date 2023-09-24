#!/usr/bin/python3
"""
Defines the city
"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    City
    """
    __tablename__: str = "cities"
    id: Column = Column(Integer, primary_key=True, nullable=False)
    name: Column = Column(String(128), nullable=False)
    state_id: Column = Column(Integer, ForeignKey("states.id"), nullable=False)
