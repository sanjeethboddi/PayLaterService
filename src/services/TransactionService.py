from exceptions.InvalidAmountExcepion import InvalidAmountExcepion
from exceptions.LowCreditException import LowCreditException
from services.UserManagementService import UserManagementService
from services.AccountingService import AccountingService
from services.MerchantManagementService import MerchantManagementService

class TransactionService:
    # __transactions = []

    @classmethod
    def make_transaction(cls, user_id, merchant_id, amount):
        if type(amount) is not float:
            raise InvalidAmountExcepion("Invalid Amount!!")
        user = UserManagementService.get_user(user_id)
        merchant = MerchantManagementService.get_merchant(merchant_id)
        merchant_discount = merchant.get_discount()
        credit_limit = user.get_credit_limit()
        current_due = AccountingService.get_user_due(user_id)

        if credit_limit < current_due + amount:
            raise LowCreditException("Low Credit Exception")
        
        updated_due = current_due + amount
        AccountingService.update_user_due(user_id, updated_due)

        discount_amount = AccountingService.get_discount_amount_received(merchant_id)
        updated_discount_amount = discount_amount + amount * (merchant_discount / 100)
        AccountingService.update_discount_amount_received(merchant_id, updated_discount_amount)
        # transaction = Transaction(user_id, merchant_id, amount)
        # cls.__transactions.append(transaction)
        
        
            
