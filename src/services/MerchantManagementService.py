from exceptions.MerchantAlreadyExistsException import MerchantAlreadyExistsException
from exceptions.InvalidDiscountException import InvalidDiscountException
from exceptions.MerchantNotFoundException import MerchantNotFoundException
from model.Merchant import Merchant
class MerchantManagementService:
    __Merchants = dict()

    @classmethod
    def create_merchant(cls, merchant_id, email, discount):
        if merchant_id in cls.__Merchants:
            raise MerchantAlreadyExistsException("Merchant Already Exists!!")
        if type(discount) is not float or discount < 0 or discount > 100:
            raise InvalidDiscountException("Invalid Discount Percentage!!")
        merchant =  Merchant(merchant_id, email, discount) 
        cls.__Merchants[merchant_id] = merchant
        return merchant
    
    @classmethod
    def get_merchant(cls, merchant_id):
        if merchant_id not in cls.__Merchants:
            raise MerchantNotFoundException("Merchant Not Found!!")
        return cls.__Merchants[merchant_id]
    # @classmethod
    # def get_all_merchants(cls):
    #     return list(cls.__Merchants.values())
