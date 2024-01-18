import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, relationship, Session
from model_state import Base, State  

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id[0], state.name[0]))
    session.close()