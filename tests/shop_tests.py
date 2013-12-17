from nose.tools import *
import grocerytrends.shop as shop

def shop_init_tests():
    print ("Testing the Province Class")
    
    quebec = shop.Province("Quebec", "QC", 13) 
    
    print ('Province Name: ' + quebec.name)
    print ('Province Abbreviation: ' + quebec.abbreviation)
    
    quebec.taxes += 45
    print ('Province Taxes (+45): {}'.format(quebec.taxes))
    
    quebec.taxes -= 45
    print ('Province Taxes(-45): {}'.format(quebec.taxes))
    
    print ("Testing the GroceryStore Class")
    loblaws = shop.GroceryStore("Loblaws", quebec)
    print ('Grocery Store Name: ' + loblaws.name)
    print ('Grocery Store Province Name: ' + loblaws.province.name)
    print ('Grocery Store Province Abbr: ' + loblaws.province.abbreviation)
    print ('Grocery Store Province Taxes: {}'.format(loblaws.province.taxes))
    
    
    print ("Testing the Receipt Class")
    receipt = shop.Receipt(loblaws)
    print ('Receipt : {}'.format(receipt.total))
    print ('Receipt Purchase Date : {}'.format(receipt.purchase_date))
    print ('Receipt Tax: {}'.format(receipt.tax))
    print ('Receipt Items: {}'.format(receipt.items))
    
    
    print ('Receipt Grocery Store Name: ' + 
           receipt.grocery_store.name)
    print ('Receipt Grocery Store Province Name: ' + 
           receipt.grocery_store.province.name)
    print ('Receipt Grocery Store Province Abbr: ' + 
           receipt.grocery_store.province.abbreviation)
    print ('Receipt Grocery Store Province Taxes: '
           '{}'.format(receipt.grocery_store.province.taxes))
    
    print ("Modifying Receipt Grocery Store Province Taxes")
    receipt.grocery_store.province.taxes += 88
    print (' '.join(["Printing Province Taxes: ", quebec.name, 
                     'taxes =', str(quebec.taxes)]
                    )
           )
    print ('Receipt Tax: {}'.format(receipt.tax))