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
from user import User
import localization
from receipt import Receipt
from localization import create_province, Store, Province

db_exists = os.path.isfile('test.db')

db = 'sqlite:///:memory:'
db = 'sqlite:///test.db'

session = db_init(db)

if not db_exists:
    populate_all_tables(session)

print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")

#session_user = login(session)
session_user = User('Jacob', 'Hooey', 'jhooey')
province = session.query(localization.Province).filter(Province.abbreviation == 'QC').first() 
default_store = Store('Metro', '94 montreal road', province)
session.add_all([session_user,default_store])
session.commit()
session_user.receipts = [Receipt(default_store)]
session.commit()
print ("Welcome, " + str(session_user))
