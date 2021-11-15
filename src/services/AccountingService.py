from exceptions.InvalidAmountExcepion import InvalidAmountExcepion
from collections import defaultdict

class AccountingService:
    __dues = defaultdict(float)
    __discount_amount_received = defaultdict(float)
    
    @classmethod
    def update_user_due(cls, user_id, amount):
        cls.__dues[user_id] = amount
    
    @classmethod
    def update_discount_amount_received(cls, merchant_id, amount):
        if type(amount) is not float:
            raise InvalidAmountExcepion("Invalid Discount Amount!")
        cls.__discount_amount_received[merchant_id] = amount
    
    @classmethod
    def get_user_due(cls, user_id):
        return cls.__dues[user_id]
    
    @classmethod
    def get_discount_amount_received(cls, merchant_id):
        return cls.__discount_amount_received[merchant_id]
