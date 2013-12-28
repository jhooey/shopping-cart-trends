from database import Base
from sqlalchemy import Column, Integer, String, Sequence, Float

class Province(Base):
    """Physical Location, used to separate different tax regions"""
    __tablename__ = 'provinces'

    id = Column(Integer, Sequence('province_id_seq'), primary_key=True)
    name = Column(String(50))
    abbreviation = Column(String(10))
    taxes = Column(Float())
    
    def __init__(self, name, abbr, taxes):
        self.name = name
        self.abbreviation = abbr
        self.taxes = float(taxes)
        

class Store(object):
    """Physical Location where the Receipt was created"""
    
    def __init__(self, name, province):
        self.name = name
        self.province = province
     

def create_province(session):
    """Gathers all the necessary info to create a new province"""
    print("What is the name of the province?")
    province_name = raw_input('> ')
    print("What is the abbreviation for the province?")
    province_abbr = raw_input('> ')
    print("What is the tax rate in % for this province?")
    province_taxes = float(raw_input('> '))

    session.add(Province(province_name, province_abbr, province_taxes))
    session.commit()

def create_store(province):
    """Gathers all the necessary info to create a new store"""
    print("What is the name of the store?")
    store_name = raw_input('> ')

    return receipt.Store(store_name, province)