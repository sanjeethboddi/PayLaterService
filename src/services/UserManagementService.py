from exceptions.InvalidCreditLimitException import InvalidCreditLimitException
from exceptions.UserAlreadyExistsException import UserAlreadyExistsException
from exceptions.InvalidEmailException import InvalidEmailException
from exceptions.UserNotFoundException import UserNotFoundException
from services.AccountingService import AccountingService
from utils.Utils import Utils

from model.User import User
class UserManagementService:
    __users = dict()
    @classmethod
    def create_user(cls, user_id, email, credit_limit):
        if user_id in cls.__users:
            raise UserAlreadyExistsException("User Already Exists!!")
        if not Utils.validate_email(email):
            raise InvalidEmailException("Invalid Email!!")
        if type(credit_limit) is not float or credit_limit<0:
            raise InvalidCreditLimitException("Invalid Credit Limit!!")
        user = User(user_id, email, credit_limit)
        cls.__users[user_id] = user
        return user
    @classmethod
    def get_user(cls,user_id):
        if user_id not in cls.__users:
            raise UserNotFoundException("User Not Found !!")
        return cls.__users[user_id]
    
    @classmethod
    def get_users_at_credit_limit(cls):
        return [user for user in cls.__users.values() if user.get_credit_limit() == AccountingService.get_user_due(user.get_username())]
    
    @classmethod
    def get_total_dues(cls):
        return [AccountingService.get_user_due(user) for user in cls.__users] 

    @classmethod
    def get_users(cls):
        return list(cls.__users.values())

