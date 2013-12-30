import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shoppingtrends.database import Base
from shoppingtrends.localization import Province, Store


class test_Province(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)
        
        self.quebec = Province('Quebec','QC', 14.975)
        self.ontario = Province('Ontario','ON', 13)
        
        self.session.add(self.quebec)
        self.session.add(self.ontario)
        
        self.session.commit()
    
    def tearDown(self):
        Base.metadata.drop_all(self.engine)
    
    def test_province_query(self):
        province = self.session.query(Province).\
                                    filter_by(name='Quebec').first()
        
        self.assertEqual(province.abbreviation, 'QC')
        self.assertAlmostEqual(province.taxes,14.975)

class test_Store(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)
        
        self.quebec = Province('Quebec','QC', 14.975)
        self.ontario = Province('Ontario','ON', 13)
        
        self.quebec.stores.append(Store('Metro', '94 Montreal rd'))

        self.loblaws = Store('loblaws', '24 Wellington st')
        
        
        self.session.add(self.quebec)
        self.session.add(self.ontario)
        self.session.add(self.loblaws)
        
        self.session.commit()
    
    def tearDown(self):
        Base.metadata.drop_all(self.engine)
    
    def test_store_relations(self):
        self.loblaws.province = self.ontario
        self.session.commit()
        
        metro_qc = self.session.query(Store).\
                                    filter_by(name='Metro').first()
        self.assertEqual(metro_qc.province.abbreviation, 'QC')
        
        loblaws_on = self.session.query(Store).\
                                    filter_by(name='loblaws').first()
        self.assertEqual(loblaws_on.province.abbreviation, 'ON')
        
        