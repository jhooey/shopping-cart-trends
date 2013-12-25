"""
The Main Program

This is the file that will be run when the application is started. 
Its function is to connect all the pieces of the application so that we 
end up with a useful piece of software.
"""
from database import db_init
from authorization import login
from localization import create_province

import user
import receipt

db_init()

print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")

session_user = login()

print ("Welcome, " + str(session_user))


create_province()