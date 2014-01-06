"""
This module contains everything necessary to describe your latest 
shopping trip.

The main purpose of this module is to give you everything you need to 
create and maintain a Receipt object. You can create item objects that 
can be attached to your receipt
"""
from sqlalchemy import Column, Integer, String, Sequence, Float, Date, Boolean
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
    __tablename__ = 'receipts'
    
    id = Column(Integer, Sequence('receipt_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    store_id = Column(Integer, ForeignKey('stores.id'))
    purchase_date = Column(Date)
    tax = Column(Float())
    
    store = relationship("Store", backref='receipts')
    items = relationship("ReceiptItem", backref="receipt")
    
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
    
    def add_item(self, session, item):
        """Appends and commits the change to the db"""
        self.items.append(item)
        session.commit()

    def remove_item(self, session, item):
        session.delete(item)
        session.commit()


class Category(Base):
    """Collections of related Items"""
    
    __tablename__ = "categories"
    
    id = Column(Integer, Sequence('cat_seq_id'), primary_key=True)
    name = Column(String(50))
    description = Column(String(500))
    
    items = relationship("Item", backref="category")
    
    def __init__(self, name, description = ""):
        self.name = name
        self.description = description
    
class Item(Base):
    
    """Generic Item, can be used to create Receipt Items"""
    __tablename__ = "items"
    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column(String(50))
    description = Column(String(500))
    taxed = Column(Boolean())
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    def __init__(self, name, description, taxed=True):
        self.name = name
        self.description = description
        self.taxed = True


        
class ReceiptItem(Base):
    """A single item purchased at a Store"""
    __tablename__ = 'receipt_items'
    
    id = Column(Integer, Sequence('r_item_id_seq'), primary_key=True)
    receipt_id = Column(Integer, ForeignKey('receipts.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    price = Column(Float())
    quantity = Column(Float())
    
    item = relationship("Item", backref='receipt_items')
    
    def __init__(self, item, price, quantity=1):
        self.item = item
        self.price = float(price)
        self.quantity = float(quantity)
    
    def __str__(self):
        return ' '.join([self.item.name, str(self.price) + '$',
                         'QTY:', str(self.quantity) ])
    
    def total_cost(self,tax):
        """
        returns the total_cost of an item based on price, 
        quantity and taxes
        
        tax must be a float
        """
        if self.item.taxed:
            return (self.quantity * self.price) * (1 + tax/100)
        else:
            return (self.quantity *self.price)