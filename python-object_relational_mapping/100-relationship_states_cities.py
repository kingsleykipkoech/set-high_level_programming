#!/usr/bin/python3
"""Creates the State 'California' with the City 'San Francisco'."""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_state = State(name="California")
    new_state.cities.append(City(name="San Francisco"))
    session.add(new_state)
    session.commit()
    session.close()
