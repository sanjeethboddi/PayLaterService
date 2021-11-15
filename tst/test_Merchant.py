import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import unittest
from model.Merchant import Merchant


class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.m1 = Merchant("m1","m@m.com",2)
        self.m2 = Merchant("m2","b@m.com",3)

    def tearDown(self):
        pass

    def test_get_merchant_id(self):
        self.assertEqual(self.m1.get_merchant_id(), "m1")
        self.assertEqual(self.m2.get_merchant_id(), "m2")
    
    def test_get_email(self):
        self.assertEqual(self.m1.get_email(), "m@m.com")
        self.assertEqual(self.m2.get_email(), "b@m.com")

    def test_get_discount(self):
        self.assertEqual(self.m1.get_discount(), 2)
        self.assertEqual(self.m2.get_discount(), 3)
    
    def test_set_discount(self):
        m3 = Merchant("m3","m@m.com",2)
        m3.set_discount(5) 
        self.assertEqual(m3.get_discount(),5)

if __name__ == '__main__':
    unittest.main()