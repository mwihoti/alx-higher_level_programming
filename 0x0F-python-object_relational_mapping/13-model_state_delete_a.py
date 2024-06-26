#!/usr/bin/python3
"""Deletes the State object "Louisiana" from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for delState in session.query(State).filter(State.name.like('%a%')):
        session.delete(delState)
    session.commit()
