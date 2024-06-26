#!/usr/bin/python3
"""Creates State “California” with the City “San Francisco” from database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
import sys
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')

    new_city = City(name='San Francisco')
    state.cities.append(new_city)
    session.add(state)
    session.commit()
    session.close()
