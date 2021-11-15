import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from services.MerchantManagementService import MerchantManagementService
from exceptions.LowCreditException import LowCreditException
from services.UserManagementService import UserManagementService
from exceptions.InvalidAmountExcepion import InvalidAmountExcepion
from services.TransactionService import TransactionService
from services.AccountingService import AccountingService
import unittest


class TestTransactionService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        UserManagementService.create_user("u1", "u@u.com", 1000.0)
        UserManagementService.create_user("u2", "u@u.com", 1000.0)
        MerchantManagementService.create_merchant("m1","m@m.co",2.0)

    def tearDown(self):
        pass

    def test_make_transaction_raises_InvalidAmountException(self):
        self.assertRaises(InvalidAmountExcepion, TransactionService.make_transaction,"u1","m1","sfa")

    def test_make_transaction_raises_LowCreditException(self):
        self.assertRaises(LowCreditException, TransactionService.make_transaction,"u1","m1",5000.0)

    


if __name__=="__main__":
    unittest.main()