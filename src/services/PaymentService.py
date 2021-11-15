from services.UserManagementService import UserManagementService
from services.MerchantManagementService import MerchantManagementService
from services.AccountingService import AccountingService

class PaymentService:
    @classmethod
    def make_payment(cls, user_id, amount):
        current_due = AccountingService.get_user_due(user_id)
        updated_user_due = current_due - amount
        AccountingService.update_user_due(user_id, updated_user_due)
        

