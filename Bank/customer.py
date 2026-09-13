from Bank.account import Account

class customer(Account):

    def deposit(self,amount):
        self._balance=self._balance+amount
        self._transaction_history.append(f"Deposit  amount {amount:7} available balance {self._balance:7}")
        
        print(f"{amount} deposited ")

    def withdraw(self,amount):

            if self._balance<amount:
                 raise ValueError("insufficient funds unable to proceed transaction")

            self._balance=self._balance-amount
            self._transaction_history.append(f"Withdraw amount {amount:7} available balance {self._balance:7}")
            print(f"{amount} withdrawed ")

    def transfer(self,amount,target_account):

         self.withdraw(amount)
         target_account.deposit(amount)
         self._transaction_history.append(f"Transferred amount {amount:7} available balance {self._balance:7}")

         print(f"{amount} transferred succesfully")
         

    
        
