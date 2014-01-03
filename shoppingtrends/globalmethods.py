def ask_yes_no_question():
    """Asks the user to answer yes or no, returns a boolean"""
    while True:
        answer = raw_input('Yes or No? ')
        
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return True
        if answer.lower() == 'no' or  answer.lower() == 'n':
            return False
        

def create_province():
    """Gathers all the necessary info to create a new province"""
    print("What is the name of the province?")
    province_name = raw_input('> ')
    print("What is the abbreviation for the province?")
    province_abbr = raw_input('> ')
    print("What is the tax rate in % for this province?")
    province_taxes = float(raw_input('> '))
    
    return Province(province_name, province_abbr, province_taxes)

def create_store():
    """Gathers all the necessary info to create a new store"""
    print("What is the name of the store?")
    store_name = raw_input('> ')

    return receipt.Store(store_name)
 
       
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