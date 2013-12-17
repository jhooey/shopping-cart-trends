"""
This module contains everything necessary to describe your latest shopping
trip.

The main purpose of this module is to give you everything you need to create
and maintain a Receipt object. You can specify which Grocery Store you were 
shopping at and in which Province the Store is locate. Most importantly you 
can create item objects that can be attached to your receipt
"""


import datetime

class Province(object):
    """Physical Location, used to separate different tax regions"""
    
    def __init__(self, name, abbr, taxes):
        self.name = name
        self.abbreviation = abbr
        self.taxes = taxes
        

class Store(object):
    """Physical Location where the Receipt was created"""
    
    def __init__(self, name, province):
        self.name = name
        self.province = province
        
class Receipt(object):
    """
    Collection of Items describing a trip to a store
    
    Records the tax rate at the time of entry so that it does not change if 
    the provincial tax rate changes.
    """
    
    def __init__(self, store, purchase_date=datetime.date.today()):
        self.store = store
        self.purchase_date = purchase_date
        
        self.total = 0
        self.items = []
        
        self.tax = store.province.taxes
        
class Item(object):
    """A single item purchased at a Store"""
    
    def __init__(self, name, price, taxed=False):
        self.name = name
        self.price = price