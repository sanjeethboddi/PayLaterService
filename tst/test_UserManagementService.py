import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from exceptions.UserAlreadyExistsException import UserAlreadyExistsException
from exceptions.UserNotFoundException import UserNotFoundException
from exceptions.InvalidCreditLimitException import InvalidCreditLimitException
from services.UserManagementService import UserManagementService
from services.AccountingService import AccountingService
import unittest


class TestUserManagementService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        UserManagementService.create_user('u1', 'u@a.co', 1000.0)
        UserManagementService.create_user('u2', 'u@a.co', 1000.0)
        UserManagementService.create_user('u3', 'u@a.co', 1000.0)
        UserManagementService.create_user('u4', 'u@a.co', 1000.0)
        UserManagementService.create_user('u5', 'u@a.co', 0.0)
        UserManagementService.create_user('u6', 'u@a.co', 1.0)
        AccountingService.update_user_due('u3',500.0)
        AccountingService.update_user_due('u4',1000.0)
        
        
    def tearDown(self):
        pass
    def test_create_user_raises_UserAlreadyExistsException(self):
        
        self.assertRaises(UserAlreadyExistsException, UserManagementService.create_user, 'u1', 'u@a.co', 1000.0)
    def test_create_user_raises_InvalidCreditLimitException(self):
        self.assertRaises(InvalidCreditLimitException, UserManagementService.create_user, 'u7', 'u@a.co', 1000)
        self.assertRaises(InvalidCreditLimitException, UserManagementService.create_user, 'u7', 'u@a.co', "100")
    
    def test_get_user_raises_UserNotFoundException(self):
        self.assertRaises(UserNotFoundException, UserManagementService.get_user, 'u7')

    def test_get_user(self):
        user =  UserManagementService.get_user('u3')
        self.assertEqual(user.get_username(), 'u3')
    
    def test_get_users_at_credit_limit(self):
        size = len(UserManagementService.get_users_at_credit_limit())
        self.assertEqual(size,2)
        
    def test_get_total_dues(self):
        self.assertEqual(1500.0,sum(UserManagementService.get_total_dues()))
    
    def test_get_users(self):
        self.assertEqual(6,len(UserManagementService.get_users()))


if __name__=="__main__":
    unittest.main()