class Merchant:
    def __init__(self, merchant_id, email, discount):
        self.__merchant_id = merchant_id
        self.__email = email
        self.__discount = discount
    
    def set_discount(self, discount):
        self.__discount = discount
    
    def get_merchant_id(self):
        return self.__merchant_id
    
    def get_discount(self):
        return self.__discount

    def get_email(self):
        return self.__email

    def __str__(self):
        return self.__merchant_id+"("+str(self.__discount)+"%)"
    
    