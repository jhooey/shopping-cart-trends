"""
The Main Program

This is the file that will be run when the application is started. 
Its function is to connect all the pieces of the application so that we 
end up with a useful piece of software.
"""
from database import db_init
from authorization import login
from localization import create_province, Store

session = db_init()

print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")

#session_user = login(session)

#print ("Welcome, " + str(session_user))


province = create_province()

province.stores.append(Store('Metro'))

loblaws = Store('loblaws')

session.add(province)
session.add(loblaws)
session.commit()

loblaws.province = province

session.commit()