from database import Base
from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Country(Base):
    """Physical Location, separated into different governmental bodies"""
    __tablename__ = 'countries'

    id = Column(String(3), primary_key=True)
    name = Column(String(50))
    
    provinces = relationship("Province", backref="country")
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Province(Base):
    """Physical Location, used to separate different tax regions"""
    __tablename__ = 'provinces'

    id = Column(Integer, Sequence('province_id_seq'), primary_key=True)
    name = Column(String(50))
    abbreviation = Column(String(10))
    taxes = Column(Float())
    country_code = Column(String(3), ForeignKey('countries.id'))
    
    def __init__(self, name, abbr, taxes):
        self.name = name
        self.abbreviation = abbr
        self.taxes = float(taxes)
        

class Store(Base):
    """Physical Location where the Receipt was created"""
    __tablename__ = 'stores'
    
    id = Column(Integer, Sequence('store_id_seq'), primary_key=True)
    name = Column(String(50))
    address = Column(String(100))
    province_id = Column(Integer, ForeignKey('provinces.id'))
    
    province = relationship("Province", backref=backref('stores', 
                                                        order_by=id))
    
    
    def __init__(self, name, address):
        self.name = name
        self.address = address

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