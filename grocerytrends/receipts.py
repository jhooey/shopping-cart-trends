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
        self.taxes = float(taxes)
        

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
        self.items = []
        self.tax = store.province.taxes
    
    def __str__(self):
        str_out = 'Receipt: \n'
        str_out += ' '.join([self.store.name, '    ', str(self.purchase_date), '\n' ])
        for item in self.items:
            str_out += ' '.join(['\n', str(item), '    ', 
                            str(round(item.total_cost(self.tax),2))])
        str_out += ' '.join(['\n\nTaxes:', str(self.tax), 
                             '    Total =', str(round(self.total(),2))])
        return str_out
        
    
    def total(self):
        total = 0
        for item in self.items:
            total += item.total_cost(self.tax)
        return total
    
    def add_item(self, item):
        self.items.append(item)
        
        
class Item(object):
    """A single item purchased at a Store"""
    
    def __init__(self, name, price, quantity=1, taxed=False):
        self.name = name
        self.price = float(price)
        self.quantity = float(quantity)
        self.taxed = taxed
    
    def __str__(self):
        return ' '.join([self.name, str(self.price) + '$',
                         'QTY:', str(self.quantity) ])
       
    def total_cost(self,tax):
        if self.taxed:
            return (self.quantity * self.price) * (1 + tax/100)
        else:
            return (self.quantity *self.price)