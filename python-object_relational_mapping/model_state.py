from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define the Base instance
Base = declarative_base()

class State(Base):
    """Class representing the 'states' table in MySQL."""

    __tablename__ = 'states'

    # Columns definition
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Create a SQLite engine (you can replace this with your MySQL connection)
#engine = create_engine('sqlite:///:memory:', echo=True)

# Import the State class before calling create_all
#Base.metadata.create_all(engine)
