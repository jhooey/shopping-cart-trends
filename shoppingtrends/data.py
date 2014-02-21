from localization import Province, Country, Store
from user import User
from receipt import Receipt, Item
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
    
    loblaws = Store("Loblaws", "Rideau and Nelson", ontario)
    Maxi = Store("Maxi", "Hull St. Joseph", quebec)
    
    loblaws_receipt1 = Receipt(loblaws)
    loblaws_receipt2 = Receipt(loblaws, datetime.date.fromordinal(datetime.date.today().toordinal()-1))
    loblaws_receipt3 = Receipt(loblaws, datetime.date.fromordinal(datetime.date.today().toordinal()-4))
    
    bananas = Item('Bananas', 'yellow fruit', False)
    napkins = Item('Napkins', 'paper napkins', True)
    
    session.add_all([loblaws,
                     Maxi,
                     Store("Herb and Spice Shop", "375 Bank Street", ontario),
                     User("Jacob", "Hooey", "jhooey", "password"),
                    loblaws_receipt1,
                    loblaws_receipt2,
                    loblaws_receipt3,
                    bananas,
                    napkins],
                    )




    session.commit()

