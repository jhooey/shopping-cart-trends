import receipt
import user

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
    
#def create_receipt():
#    new_item = True
#   while new_item:
#       print("Do you have another Item to add?")
#       new_item = ask_yes_no_question()

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


print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")
print("What's your first name?")
first_name = raw_input('> ')
print("What's your last name?")
last_name = raw_input('> ')
print("What do you want as your username?")
username = raw_input('> ')

user1 = user.User(first_name, last_name, username)

print (str(user1))

print (str(create_item().total_cost(13.0)))
print (str(create_item().total_cost(13.0)))