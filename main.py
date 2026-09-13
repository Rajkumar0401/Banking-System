from Bank.customer import customer
Active_accounts={}

Customer1=customer("Raj",5000,Active_accounts)
Active_accounts[Customer1.account_number]=Customer1
Customer2=customer("Uday",10000,Active_accounts)
Active_accounts[Customer2.account_number]=Customer2
Customer1.withdraw(1000)