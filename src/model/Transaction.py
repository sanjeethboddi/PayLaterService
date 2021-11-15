class Transaction:
    def __init__(self, user_id, merchant_id, amount):
        self.__user_id = user_id
        self.__merchant_id = merchant_id
        self.__amount = amount
    
    def get_user_id(self):
        return self.__user_id
    def get_merchant_id(self):
        return self.__merchant_id
    def get_amount(self):
        return self.__amount