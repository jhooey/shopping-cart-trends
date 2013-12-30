from database import Base
from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Province(Base):
    """Physical Location, used to separate different tax regions"""
    __tablename__ = 'provinces'

    id = Column(Integer, Sequence('province_id_seq'), primary_key=True)
    name = Column(String(50))
    abbreviation = Column(String(10))
    taxes = Column(Float())
    
    #stores = relationship("Store", 
    #                      order_by="Store.id", 
    #                      backref="province")
    
    def __init__(self, name, abbr, taxes):
        self.name = name
        self.abbreviation = abbr
        self.taxes = float(taxes)
        

class Store(Base):
    """Physical Location where the Receipt was created"""
    __tablename__ = 'stores'
    
    id = Column(Integer, Sequence('store_id_seq'), primary_key=True)
    name = Column(String(50))
    province_id = Column(Integer, ForeignKey('provinces.id'))
    
    province = relationship("Province", backref=backref('stores', 
                                                        order_by=id))
    
    
    def __init__(self, name):
        self.name = name
     

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