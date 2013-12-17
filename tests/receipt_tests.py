from nose.tools import *
import unittest
import grocerytrends.receipt as receipt

def setup_func():
    quebec = receipt.Province("Quebec", "QC", 13)
    loblaws = receipt.Store("Loblaws", quebec) 
    
    
    global loblaws_receipt
    loblaws_receipt = receipt.Receipt(loblaws)
    
    global bananas
    bananas = receipt.Item('Bananas', 0.79, 1.8)
    pears = receipt.Item('Pears', 1.49, 4)
    napkins = receipt.Item('Napkins', 2.0, 1, True)

def teardown_func():
    quebec = None
    loblaws = None
    loblaws_receipt = None
    
    bananas = None
    pears = None
    napkins = None

@with_setup(setup_func, teardown_func)
def test_Receipt_add_item():
    assert not loblaws_receipt.items
    loblaws_receipt.add_item(bananas)
    assert loblaws_receipt.items