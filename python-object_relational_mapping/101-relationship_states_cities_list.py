#!/usr/bin/python3
"""Script that lists all the State objects and their City objects."""
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, joinedload, relationship
from sqlalchemy.orm import sessionmaker
import sys

try:
    from relationship_city import City
    from relationship_state import Base, State
except ImportError:
    Base = declarative_base()

    class State(Base):
        """State class linked to the table states and to its cities."""

        __tablename__ = "states"

        id = Column(Integer, primary_key=True, autoincrement=True,
                    nullable=False)
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", order_by="City.id",
                              cascade="all, delete-orphan")

    class City(Base):
        """City class that represents a row of the table cities."""

        __tablename__ = "cities"

        id = Column(Integer, primary_key=True, autoincrement=True,
                    nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    states = session.query(State).options(joinedload(State.cities))
    for state in states.order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
