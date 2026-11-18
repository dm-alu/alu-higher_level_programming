#!/usr/bin/python3
"""Module that defines the State class with its cities relationship."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class linked to the table states and to its cities."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", order_by="City.id",
                          cascade="all, delete-orphan")
