from nose.tools import *
from grocerytrends.shopping import Province, GroceryStore, Receipt

def test_grocery_store():
    print ("Testing the Receipt Class")
    quebec = Province("Quebec", "QC", 13)
    
    loblaws = GroceryStore("Loblaws", quebec)
    
    receipt = Receipt(loblaws)
    print (receipt.total)
    print (receipt.tax)
    print (receipt.items)