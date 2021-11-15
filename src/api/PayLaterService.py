from services.AccountingService import AccountingService
from services.PaymentService import PaymentService
from services.TransactionService import TransactionService
from services.UserManagementService import UserManagementService
from services.MerchantManagementService import MerchantManagementService


class PayLaterService:
    @staticmethod
    def create_new_user(*args):
        try:
            user = UserManagementService.create_user(args[0],args[1],float(args[2]))  
            print(user)
        except Exception as e:
            print(e)
    
    @staticmethod
    def create_new_merchant(*args):
        try:
            merchant = MerchantManagementService.create_merchant(args[0], args[1], float(args[2].strip("%")))
            print(merchant)
        except Exception as e:
            print(e)
    
    @staticmethod
    def create_new_transaction(*args):
        try:
            TransactionService.make_transaction(args[0],args[1],float(args[2]))
        except Exception as e:
            print(e)

    @staticmethod
    def update_merchant_discount(*args):
        try:
            MerchantManagementService.get_merchant(args[0]).setDiscount(float(args[1].strip('%')))
        except Exception as e:
            print(e)
    
    @staticmethod
    def payback(*args):
        try:
            PaymentService.make_payment(args[0],float(args[1]))
        except Exception as e:
            print(e)
    
    @staticmethod
    def report_dues_of_user(*args):
        try:
            AccountingService.get_user_due(args[1])
        except Exception as e:
            print(e)
    
    @staticmethod
    def report_total_dues(*args):
        try:
            users = UserManagementService.get_users()
            dues = [(user.get_username(),AccountingService.get_user_due(user.get_username())) for user in users]
            total = 0
            for due in dues:
                print (due)
                total += due[1]
            print(total)
        except Exception as e:
            print(e)
    
    @staticmethod
    def report_users_at_credit_limit(*args):
        try:
            users_at_credit_limit = UserManagementService.get_users_at_credit_limit()
            for user in users_at_credit_limit:
                print(user)
        except Exception as e:
            print(e)

    @staticmethod
    def report_merchant_discount(*args):
        try:
            discount = MerchantManagementService.get_merchant(args[1]).get_discount()
            print(discount)
        except Exception as e:
            print(e)
