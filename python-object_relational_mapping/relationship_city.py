#!/usr/bin/python3
"""Module that defines the City class linked to the table cities."""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """City class that represents a row of the table cities."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
