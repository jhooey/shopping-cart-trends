from nose.tools import *
import grocerytrends.receipts as receipts

def receipt_init_tests():
    print ("Testing the Province Class")
    
    quebec = receipts.Province("Quebec", "QC", 13) 
    
    print ('Province Name: ' + quebec.name)
    print ('Province Abbreviation: ' + quebec.abbreviation)
    
    quebec.taxes += 45
    print ('Province Taxes (+45): {}'.format(quebec.taxes))
    
    quebec.taxes -= 45
    print ('Province Taxes(-45): {}'.format(quebec.taxes))
    
    print ("Testing the Store Class")
    loblaws = receipts.Store("Loblaws", quebec)
    print ('Store Name: ' + loblaws.name)
    print ('Store Province Name: ' + loblaws.province.name)
    print ('Store Province Abbr: ' + loblaws.province.abbreviation)
    print ('Store Province Taxes: {}'.format(loblaws.province.taxes))
    
    
    print ("Testing the Receipt Class")
    receipt = receipts.Receipt(loblaws)
    print ('Receipt : {}'.format(receipt.total()))
    print ('Receipt Purchase Date : {}'.format(receipt.purchase_date))
    print ('Receipt Tax: {}'.format(receipt.tax))
    print ('Receipt Items: {}'.format(receipt.items))
    
    
    print ('Receipt Store Name: ' + 
           receipt.store.name)
    print ('Receipt Store Province Name: ' + 
           receipt.store.province.name)
    print ('Receipt Store Province Abbr: ' + 
           receipt.store.province.abbreviation)
    print ('Receipt Store Province Taxes: '
           '{}'.format(receipt.store.province.taxes))
    
    print ("Modifying Receipt Store Province Taxes")
    receipt.store.province.taxes += 88
    print (' '.join(["Printing Province Taxes: ", quebec.name, 
                     'taxes =', str(quebec.taxes)]
                    )
           )
    print ('Receipt Tax: {}'.format(receipt.tax))
    
    print(str(receipt))


    bananas = receipts.Item('Bananas', 0.79, 1.8)
    
    print ('Item Name : {}'.format(bananas.name))
    print ('Item Price : {}'.format(bananas.price))
    print ('Item Quantity: {}'.format(bananas.quantity))
    print ('Item Taxed? {}'.format(bananas.taxed))
    
    print (str(bananas))

def receipts_method_tests():
    quebec = receipts.Province("Quebec", "QC", 13)
    loblaws = receipts.Store("Loblaws", quebec) 
    receipt = receipts.Receipt(loblaws)
    
    bananas = receipts.Item('Bananas', 0.79, 1.8)
    pears = receipts.Item('Pears', 1.49, 4)
    napkins = receipts.Item('Napkins', 2.0, 1, True)
    receipt.add_item(bananas)
    receipt.add_item(pears)
    receipt.add_item(napkins)
    
    print(str(receipt))
    
    receipt.remove_item_by_name(bananas.name)
    
    print(str(receipt))
    
    