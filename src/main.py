import sys
from services.PaymentService import PaymentService
from services.TransactionService import TransactionService
sys.path.append('model')
sys.path.append('exceptions')
sys.path.append('api')
sys.path.append('services')

from api.PayLaterService import PayLaterService

while True:
    command = input('> ')
    tokens = command.strip().split()
    if len(tokens) == 0:
        continue
    if tokens[0] == 'exit':
        break

    elif tokens[0] == 'new':
        if tokens[1] == 'user':
            PayLaterService.create_new_user(*tokens[2:])
        elif tokens[1] == 'merchant':
            PayLaterService.create_new_merchant(*tokens[2:])
        elif tokens[1] == 'txn':
            PayLaterService.create_new_transaction(*tokens[2:])
    elif tokens[0] == 'update':
        PayLaterService.update_merchant_discount(*tokens[1:])
    elif tokens[0] == 'payback':
        PayLaterService.payback(*tokens[1:])
    elif tokens[0] == 'report':
        if tokens[1] == 'dues':
            PayLaterService.report_dues(*tokens[2:])
        elif tokens[1] == 'users-at-credit-limit':
            PayLaterService.report_users_at_credit_limit(*tokens[2:])
        elif tokens[1] == 'total-dues':
            PayLaterService.report_total_dues(*tokens[2:])
        elif tokens[1] == 'discount':
            PayLaterService.report_merchant_discount(*tokens[2:])

