from nose.tools import *
from grocerytrends.shopping import Province
from grocerytrends.shopping import GroceryStore

def test_grocery_store():
    print ("Testing the GroceryStore Class")
    quebec = Province("Quebec", "QC", 13)
    
    loblaws = GroceryStore("Loblaws", quebec)
    
    print (loblaws.name)
    print (loblaws.province.name)
    print (loblaws.province.abbreviation)
    print (loblaws.province.taxes)