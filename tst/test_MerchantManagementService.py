import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from exceptions.MerchantAlreadyExistsException import MerchantAlreadyExistsException
from exceptions.MerchantNotFoundException import MerchantNotFoundException
from exceptions.InvalidDiscountException import InvalidDiscountException
from services.MerchantManagementService import MerchantManagementService


from services.AccountingService import AccountingService
import unittest


class TestMerchantManagementService(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_merchant_raises_MerchantAlreadyExistsException(self):
        MerchantManagementService.create_merchant("m1","m@c.co",2.0)
        self.assertRaises(MerchantAlreadyExistsException, MerchantManagementService.create_merchant, "m1", "m@c.co", 2.0)

    def test_create_merchant_raises_InvalidDiscountException(self):
        self.assertRaises(InvalidDiscountException, MerchantManagementService.create_merchant, "m1", "m@c.co", 2)
        self.assertRaises(InvalidDiscountException, MerchantManagementService.create_merchant, "m1", "m@c.co", "2.0")
        self.assertRaises(InvalidDiscountException, MerchantManagementService.create_merchant, "m1", "m@c.co", 102.0)

    def test_get_merchant_raises_MerchantNotFoundException(self):
        self.assertRaises(MerchantNotFoundException, MerchantManagementService.get_merchant, "m2")
    
    def test_get_merchant_succeeds(self):
        MerchantManagementService.create_merchant("m3","m@c.co",2.0)
        merchant = MerchantManagementService.get_merchant('m3')
        self.assertEqual(merchant.get_merchant_id(), 'm3')


if __name__=="__main__":
    unittest.main()