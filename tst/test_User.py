import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import unittest

from model.User import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user1 = User("user1","sss@aaa.com",1000)
        self.user2 = User("user2","sss@aba.com",100)

    def tearDown(self):
        pass

    def test_get_username(self):
        self.assertEqual(self.user1.get_username(),"user1")
        self.assertEqual(self.user2.get_username(),"user2")

    def test_get_credit_limit(self):
        self.assertEqual(self.user1.get_credit_limit(),1000)
        self.assertEqual(self.user2.get_credit_limit(),100)

    def test_get_email(self):
        self.assertEqual(self.user1.get_email(),"sss@aaa.com")
        self.assertEqual(self.user2.get_email(),"sss@aba.com")


if __name__ == '__main__':
    unittest.main()