#!/usr/bin/python3
# Deletes the State object "Louisiana" from the database hbtn_0e_6_usa.
# Usage: ./script_name.py <mysql username> <mysql password> <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana_state = session.query(State).filter_by(name="Louisiana").first()
    
    if louisiana_state:
        # Delete the "Louisiana" state object
        session.delete(louisiana_state)
        session.commit()
        print("Louisiana state object deleted successfully.")
    else:
        print("Louisiana state object not found.")
