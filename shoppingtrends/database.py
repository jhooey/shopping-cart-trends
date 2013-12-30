"""
This module handles the setup of the database and sessions
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Use by the classes to declare a mapping
Base = declarative_base()


def db_init(conn_str):
    engine = create_engine(conn_str, echo=True)
    
    """Sets all the initial database requirements"""
    #This initializes all of the tables in the DB
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    return Session()