import datetime

class Province(object):
    
    def __init__(self, name, abbr, taxes):
        self.name = name
        self.abbreviation = abbr
        self.taxes = taxes
        

class GroceryStore(object):
    
    def __init__(self, name, province):
        self.name = name
        self.province = province
        
class Receipt(object):
    
    def __init__(self, grocery_store, purchase_date=datetime.date.today()):
        self.grocery_store = grocery_store
        self.purchase_date = purchase_date
        
        self.total = 0
        self.items = []
        
        self.tax = grocery_store.province.taxes
        
class Item(object):
    
    def __init__(self, name, price, taxed=False):
        self.name = name
        self.price = price