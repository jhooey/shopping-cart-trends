from database import Base, engine
from sqlalchemy.orm import sessionmaker

import user

def login():
    print("What is your username?")
    session_user = session.query(user.User).filter_by(
                                                      username=raw_input('> ')
                                                      ).first() 
    if session_user:
        return check_pwd(session_user), session_user
    else:
        print("Sorry we could not find your username")
        return False, None 

def check_pwd(session_user):
    print("What is your password?")
    input_password = raw_input('> ')
    
    return input_password == session_user.password


def create_user():
    print("What's your first name?")
    first_name = raw_input('> ')
    print("What's your last name?")
    last_name = raw_input('> ')
    print("What do you want as your username?")
    username = raw_input('> ')
    
    session.add(user.User(first_name, last_name, username))
    session.commit()

def create_province():
    print("What is the name of the province?")
    province_name = raw_input('> ')
    print("What is the abbreviation for the province?")
    province_abbr = raw_input('> ')
    print("What is the tax rate in % for this province?")
    province_taxes = float(raw_input('> '))

    session.add(receipt.Province(province_name, province_abbr, province_taxes))
    session.commit()

def create_store(province):
    print("What is the name of the store?")
    store_name = raw_input('> ')

    return receipt.Store(store_name, province) 
    
def create_receipt(store):
    store_receipt = receipt.Receipt(store)
    
    new_item = True
    while new_item:
        store_receipt.add_item(create_item())
        
        print("Do you have another Item to add?")
        new_item = ask_yes_no_question()

    return store_receipt
    
def create_item():
    print("What is the name of the item?")
    item_name = raw_input('> ')
    print("What is the Price/QTY?")
    item_price = float(raw_input('> '))
    print("What is the QTY?")
    item_qty = float(raw_input('> '))
    print("Is this item taxed?")
    item_taxed = ask_yes_no_question()
    
    return receipt.Item(item_name, item_price, item_qty, item_taxed)
    
def ask_yes_no_question():
    """
    Asks the user to answer yes or no, returns true or false respectively
    """
    while True:
        answer = raw_input('Yes or No? ')
        
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return True
        if answer.lower() == 'no' or  answer.lower() == 'n':
            return False

"""
The Main Program
"""

Session = sessionmaker(bind=engine)
session = Session()


print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")

logged_in = False
    
while not logged_in:
    print("Are you registered?")
    if ask_yes_no_question():    
        logged_in, session_user = login()
    else:
        create_user()
        print("Let's restart the login process")

print ("Welcome, " + str(session_user))

create_province()

#province = create_province()
#store = create_store(province)

#print (str(create_receipt(store)))