from localization import Province, Country

def populate_all_tables(session):
    populate_provinces_tbl(session)

def populate_provinces_tbl(session):
    
    canada = Country("CAN", "Canada")
    
    
    canada.provinces = [Province('Alberta','AB', 5),
                     Province('British Columbia','BC', 12),
                     Province('Manitoba','MB', 13),
                     Province('New Brunswick','NB', 13),
                     Province('Newfoundland and Labrador','NL', 13),
                     Province('Northwest Territories','NT', 5),
                     Province('Nova Scotia','NS', 15),
                     Province('Nunavut','NU', 5),
                     Province('Ontario','ON', 13),
                     Province('Prince Edward Island','PE', 14),
                     Province('Quebec','QC', 14.975),
                     Province('Saskatchewan','SK', 10),
                     Province('Yukon','YT', 5)
                     ]
    session.add(canada)
    session.commit()
