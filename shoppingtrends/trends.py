"""
The Main Program

This is the file that will be run when the application is started. 
Its function is to connect all the pieces of the application so that we 
end up with a useful piece of software.
"""

import os.path

from database import db_init
from data import populate_all_tables
from authorization import login
from localization import create_province, Store

db_exists = os.path.isfile('test.db')

session = db_init('sqlite:///test.db')

if not db_exists:
    populate_all_tables(session)

print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")

session_user = login(session)

print ("Welcome, " + str(session_user))