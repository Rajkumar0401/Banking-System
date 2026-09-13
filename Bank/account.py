
from random import randint

def generate_unique_code(Active_accounts):

    while True:
        code=str(randint(100000,999999))

        if code not in Active_accounts:
            return code

class Account:
    def __init__(self,owner_name,balance,Active_accounts):
        self.account_number=generate_unique_code(Active_accounts)
        self._owner_name=owner_name
        self._balance=balance
        self._transaction_history=[]
        
        