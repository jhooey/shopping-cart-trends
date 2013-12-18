from nose.tools import *
import unittest
import grocerytrends.receipt as receipt


class test_Item(unittest.TestCase):
    
    def setUp(self):
        self.bananas = receipt.Item('Bananas', 0.79, 1.8)
        self.pears = receipt.Item('Pears', 1.49, 4)
        self.napkins = receipt.Item('Napkins', 2.0, 1, True)
    
    def tearDown(self):
        self.bananas = None
        self.pears = None
        self.napkins = None
    
    def test_total_cost(self):
        #Item without tax, but tax still has to be passed
        self.assertAlmostEqual(self.bananas.total_cost(13.0),1.422)

        #Item with tax
        self.assertAlmostEqual(self.napkins.total_cost(13.0), 2.26)
        

class test_Receipt(unittest.TestCase):
    
    def setUp(self):
        self.quebec = receipt.Province("Quebec", "QC", 13)
        self.loblaws = receipt.Store("Loblaws", self.quebec) 
        
        self.loblaws_receipt = receipt.Receipt(self.loblaws)
        
        self.bananas = receipt.Item('Bananas', 0.79, 1.8)
        self.napkins = receipt.Item('Napkins', 2.0, 1, True)
    
    def tearDown(self):
        self.quebec = None
        self.loblaws = None
        self.loblaws_receipt = None
        
        self.bananas = None
        self.pears = None
        self.napkins = None
    
    def test_Receipt_add_remove_item(self):
        assert not self.loblaws_receipt.items
        self.loblaws_receipt.add_item(self.bananas)
        assert self.loblaws_receipt.items
        self.loblaws_receipt.remove_item_by_name(self.bananas.name)
        assert not self.loblaws_receipt.items
        
        
    def test_Receipt_add_remove_item(self):
        self.assertAlmostEqual(self.loblaws_receipt.total(),0.0)
        
        self.loblaws_receipt.add_item(self.bananas)
        self.assertAlmostEqual(self.loblaws_receipt.total(),1.422)
        
        self.loblaws_receipt.add_item(self.napkins)
        self.assertAlmostEqual(self.loblaws_receipt.total(),3.682)
        
        self.loblaws_receipt.remove_item_by_name(self.bananas.name)
        self.assertAlmostEqual(self.loblaws_receipt.total(),2.26)

        