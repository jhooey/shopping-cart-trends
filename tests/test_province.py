from nose.tools import *
from grocerytrends.shopping import Province

def test_province():
    print ("Testing the Province class")
    
    
    quebec = Province("Quebec", "QC", 13)
    
    print (quebec.name)
    print (quebec.abbreviation)
    print (quebec.taxes)
    
    quebec.taxes += 45
    print (quebec.taxes)