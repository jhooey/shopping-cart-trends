from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db', echo=True)

#Use by the classes to declare a mapping
Base = declarative_base()

#This initializes all of the tables in the DB
#Base.metadata.create_all(engine)