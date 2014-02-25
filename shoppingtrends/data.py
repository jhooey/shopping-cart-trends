from localization import Province, Country, Store
from user import User
from receipt import Receipt, Item, Category
import datetime

def populate_all_tables(session):
    populate_provinces_tbl(session)

def populate_provinces_tbl(session):
    canada = Country("CAN", "Canada")
    
    ontario = Province('Ontario','ON', 13)
    quebec = Province('Quebec','QC', 14.975)
    
    canada.provinces = [Province('Alberta','AB', 5),
                     Province('British Columbia','BC', 12),
                     Province('Manitoba','MB', 13),
                     Province('New Brunswick','NB', 13),
                     Province('Newfoundland and Labrador','NL', 13),
                     Province('Northwest Territories','NT', 5),
                     Province('Nova Scotia','NS', 15),
                     Province('Nunavut','NU', 5),
                     ontario,
                     Province('Prince Edward Island','PE', 14),
                     quebec,
                     Province('Saskatchewan','SK', 10),
                     Province('Yukon','YT', 5)
                     ]
    session.add(canada)
    
    
    #Create test user
    jhooey = User("Jacob", "Hooey", "jhooey", "password")
    
    #Create test Stores
    loblaws = Store("Loblaws", "Rideau and Nelson", ontario)
    Maxi = Store("Maxi", "Hull St. Joseph", quebec)
    herbspice = Store("Herb and Spice Shop", "375 Bank Street", ontario)
    
    
    #Create test Receipts
    loblaws_receipt1 = Receipt(loblaws)
    loblaws_receipt2 = Receipt(loblaws, datetime.date.fromordinal(datetime.date.today().toordinal()-1))
    loblaws_receipt3 = Receipt(loblaws, datetime.date.fromordinal(datetime.date.today().toordinal()-4))
    
    #Create Test Items
    bananas = Item('Bananas', 'yellow fruit', False)
    napkins = Item('Napkins', 'paper napkins', True)
    
    #Add items to receipts
    loblaws_receipt1.add_item(session, bananas, 2, 0.79)
    loblaws_receipt1.add_item(session, napkins, 1, 2.99)
    
    loblaws_receipt2.add_item(session, bananas, 1.54, 0.79)
    
    loblaws_receipt3.add_item(session, bananas, 10.2, 0.59)
    loblaws_receipt3.add_item(session, napkins, 3, 1.99)
    
    #Add Receipts to test user
    jhooey.add_receipt(loblaws_receipt1)
    jhooey.add_receipt(loblaws_receipt2)
    jhooey.add_receipt(loblaws_receipt3)
    
    
    session.add_all([
                     loblaws,
                     Maxi,
                     herbspice,
                     jhooey,
                     bananas,
                     napkins,
                     Category('Food', 'Stuff you eat'),
                     Category('Household Supplies', "Stuff you don't eat")
                    ],
                   )

    session.commit()

