#!/usr/bin/python3
"""script that changes the name of a State object from the database
hbtn_0e_6_usa
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State).get(2)
    records.name = 'New Mexico'
    session.commit()
    session.close()
