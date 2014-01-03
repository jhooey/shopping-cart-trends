from database import Base
from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Country(Base):
    """
    Physical Location, separated into different governmental bodies
    
    Purpose: To contain a collection of provinces
    """
    __tablename__ = 'countries'

    country_code = Column(String(3), primary_key=True)
    name = Column(String(50))
    
    provinces = relationship("Province", backref="country")
    
    def __init__(self, country_code, name):
        self.country_code = country_code
        self.name = name

class Province(Base):
    """Physical Location, used to separate different tax regions"""
    __tablename__ = 'provinces'

    id = Column(Integer, Sequence('province_id_seq'), primary_key=True)
    name = Column(String(50))
    abbreviation = Column(String(10))
    taxes = Column(Float())
    country_code = Column(String(3), ForeignKey('countries.country_code'))
    
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
    
    def __init__(self, name, address, province):
        self.name = name
        self.address = address
        self.province = province