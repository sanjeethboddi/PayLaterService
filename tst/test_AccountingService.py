import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from exceptions.InvalidAmountExcepion import InvalidAmountExcepion
from services.AccountingService import AccountingService
import unittest


class TestAccountingService(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update_user_due(self):
        AccountingService.update_user_due("u1",999)
        self.assertEqual(999,AccountingService.get_user_due("u1"))

    def test_update_discount_amount_received_raises_InvalidAmountExcepion(self):
        self.assertRaises(InvalidAmountExcepion,AccountingService.update_discount_amount_received, "m1", 79)
        self.assertRaises(InvalidAmountExcepion,AccountingService.update_discount_amount_received, "m1", "79")

    def test_update_discount_amount_received(self):
        AccountingService.update_discount_amount_received("m1" , 10000.0)
        discount_m1 = AccountingService.get_discount_amount_received("m1")
        discount_m2 = AccountingService.get_discount_amount_received("m2")
        self.assertEqual(discount_m1, 10000.0)
        self.assertEqual(discount_m2, 0.0)


if __name__ == '__main__':
    unittest.main()