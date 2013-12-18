from nose.tools import *
import grocerytrends.receipt as receipt

class test_Receipt:
    
    def setUp(self):
        self.quebec = receipt.Province("Quebec", "QC", 13)
        self.loblaws = receipt.Store("Loblaws", self.quebec) 
        
        self.loblaws_receipt = receipt.Receipt(self.loblaws)
        
        self.bananas = receipt.Item('Bananas', 0.79, 1.8)
        self.pears = receipt.Item('Pears', 1.49, 4)
        self.napkins = receipt.Item('Napkins', 2.0, 1, True)
    
    def tearDown(self):
        self.quebec = None
        self.loblaws = None
        self.loblaws_receipt = None
        
        self.bananas = None
        self.pears = None
        self.napkins = None
    
    def test_Receipt_add_item(self):
        assert not self.loblaws_receipt.items
        self.loblaws_receipt.add_item(self.bananas)
        assert self.loblaws_receipt.items
