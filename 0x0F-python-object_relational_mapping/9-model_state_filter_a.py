#!/usr/bin/python3
"""cript that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    records = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)
    for record in records:
        print("{}: {}".format(record.id, record.name))
    session.close()
