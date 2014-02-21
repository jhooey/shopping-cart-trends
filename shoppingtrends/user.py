"""
This module managers everything regarding the person using the app

"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from passlib.hash import sha512_crypt
from database import Base

class User(Base):
    """The class that identifies the person using the application"""
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    password = Column(String(128))
    
    receipts = relationship("Receipt", backref="user")

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username.lower()
        self.password = sha512_crypt.encrypt(password)
    
    def __str__(self):
        return ''.join([self.first_name, ' ', self.last_name, 
                        ' (', self.username, ')'])
    
    def add_receipt(self, receipt):
        """
        Adds a receipt object to the user
        """
        self.receipts.append(receipt)
    
    def check_pwd(self, pwd):
        """Compares the given password with the one stored in the db"""
        return sha512_crypt.verify(pwd, self.password)