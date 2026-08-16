#!/usr/bin/python3
"""Contains the class definition of a City."""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """City class linked to MySQL table cities."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
