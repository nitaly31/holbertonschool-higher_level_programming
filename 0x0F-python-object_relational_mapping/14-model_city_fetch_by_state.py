#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(City.id, City.name, State.name).join(
        State, State.id == City.state_id).order_by(City.id)
    for record in records:
        print("{}: ({}) {}".format(record[2], record[0], record[1]))
    session.close()
