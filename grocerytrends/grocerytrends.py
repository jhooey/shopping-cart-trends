import receipt
import user
from database import Base, engine

from sqlalchemy.orm import sessionmaker

def create_province():
    print("What is the name of the province?")
    province_name = raw_input('> ')
    print("What is the abbreviation for the province?")
    province_abbr = raw_input('> ')
    print("What is the tax rate in % for this province?")
    province_taxes = float(raw_input('> '))

    return receipt.Province(province_name, province_abbr, province_taxes)

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

"""
print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")
print("What's your first name?")
first_name = raw_input('> ')
print("What's your last name?")
last_name = raw_input('> ')
print("What do you want as your username?")
username = raw_input('> ')

user1 = user.User(first_name, last_name, username)
"""

user1 = user.User('Jacob', 'Hooey', 'jhooey')


session.add(user1)

print (str(user1))

our_user = session.query(user.User).filter_by(first_name='Jacob').first() 
print (str(our_user))

#province = create_province()
#store = create_store(province)

#print (str(create_receipt(store)))