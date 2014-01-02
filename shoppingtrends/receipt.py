"""
This module contains everything necessary to describe your latest 
shopping trip.

The main purpose of this module is to give you everything you need to 
create and maintain a Receipt object. You can create item objects that 
can be attached to your receipt
"""
from sqlalchemy import Column, Integer, String, Sequence, Float, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from database import Base
from globalmethods import ask_yes_no_question

import datetime
import copy
        
class Receipt(Base):
    """
    Collection of Items describing a trip to a store
    
    Records the tax rate at the time of entry so that it does not change
    if the provincial tax rate changes.
    """
    __tablename__ = 'Receipts'
    
    id = Column(Integer, Sequence('receipt_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    store_id = Column(Integer, ForeignKey('stores.id'))
    purchase_date = Column(Date)
    tax = Column(Float())
    
    
    def __init__(self, store, purchase_date=datetime.date.today()):
        self.store = store
        self.purchase_date = purchase_date
        self.tax = store.province.taxes
    
    def __str__(self):
        """Creates a string that resembles a receipt form a store"""
        str_out = 'Receipt: \n'
        str_out += ' '.join([self.store.name, '    ', 
                             str(self.purchase_date), '\n' ])
        
        for item in self.items:
            str_out += ' '.join(['\n', str(item), '    ', 
                            str(round(item.total_cost(self.tax),2))])
            
        str_out += ' '.join(['\n\nTaxes:', str(self.tax), 
                             '    Total =', str(round(self.total(),2))])
        return str_out
        
    
    def total(self):
        """
        Takes the total_cost for each item and adds them to get a total
        """
        total = 0
        for item in self.items:
            total += item.total_cost(self.tax)
        return total
    
    def add_item(self, item):
        """
        Adds a COPY of the submitted item
        
        A copy is used because receipts are supposed to be snapshots 
        in time and then we can reuse the item for other receipts 
        """
        self.items.append(copy.deepcopy(item))
        
    def remove_item_by_name(self, name):
        name = name.lower()
        self.items = [item for item in self.items if item.name.lower() != name]
        
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
        """
        returns the total_cost of an item based on price, 
        quantity and taxes
        
        tax must be a float
        """
        if self.taxed:
            return (self.quantity * self.price) * (1 + tax/100)
        else:
            return (self.quantity *self.price)
        
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