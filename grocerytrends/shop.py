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
    
    def __init__(self, grocery_store):
        self.grocery_store = grocery_store
        self.total = 0
        self.tax = grocery_store.province.taxes
        self.items = []
        
class Item(object):
    
    def __init__(self, name, price, taxed=False):
        self.name = name
        self.price = price