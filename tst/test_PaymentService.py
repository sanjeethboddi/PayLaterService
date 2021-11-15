import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from services.PaymentService import PaymentService
from services.AccountingService import AccountingService
import unittest


class TestPaymentService(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_make_payment(self):
        AccountingService.update_user_due("u1", 500.0)
        PaymentService.make_payment("u1",100)
        self.assertEqual(AccountingService.get_user_due("u1"),400.0)
    

if __name__=="__main__":
    unittest.main()