from database import Base, engine
from sqlalchemy.orm import sessionmaker
from authorization import login
from localization import create_province

import user
import receipt

"""
The Main Program
"""
#This initializes all of the tables in the DB
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")

session_user = login(session)

print ("Welcome, " + str(session_user))


create_province(session)

#province = create_province()
#store = create_store(province)

#print (str(create_receipt(store)))