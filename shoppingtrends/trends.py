"""
Test file
"""

import os.path
import Tkinter as tk

from database import db_init
from data import populate_all_tables
from authorization import Authorzation
from user import User
from localization import Province, Store
from receipt import Receipt, Category, Item, ReceiptItem

"""MAIN APPLICATION - PART 1"""
db_exists = os.path.isfile('test.db')

db = 'sqlite:///:memory:'
#db = 'sqlite:///test.db'

session = db_init(db)

if not db_exists:
    populate_all_tables(session)
"""END OF MAIN APPLICATION"""


print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")

"""INITIALIZING TEST DATA"""
session_user = User('Jacob', 'Hooey', 'jhooey', 'p')

province = session.query(Province).\
                        filter(Province.abbreviation == 'QC').first() 

default_store = Store('Metro', '94 montreal road', province)

session.add_all([session_user,default_store])
session.commit()
"""TEST DATA INITIALIZED"""

"""MAIN APPLICATION - PART 2"""
login = Authorzation(session)
login.mainloop()

try:
    print str(login.session_user)
except: 
    quit()
"""END OF MAIN APPLICATION"""

"""TESTING FUNCTIONS

receipt = Receipt(default_store)
session_user.receipts = [receipt]
session.commit()

category = Category("Fruit")
item = Item("Bananas", "Long yellow fruit", False)
category.items.append(item)
session.add_all([category, item])
session.commit()

receipt_item = ReceiptItem(item, 0.79, 1.8)
session.add(receipt_item)
session.commit()


receipt.add_item(session, receipt_item)

print ("Welcome, " + str(session_user))
print (str(receipt))

receipt.remove_item(session, receipt_item)
print (str(receipt))
"""