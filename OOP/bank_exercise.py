""" Bank Exercise 
Create a 
* Bank class
* Account Class
* Customer class
The bank class should be able to hold many account.
You should be able to add new accounts.
The Account class should have relevant details.
The Customer class Should also have relevant details.
Stick to the techniques we have covered so far.
## Overloading
Add the abillity in your code to overload one or more init methods
"""


class Customer:

    def __init__(self, name, phoneNo):
            self.name = name
            self.phoneNo = phoneNo
    
    def __str__(self):
        return f"This customer is {self.name}. The phone Number is {self.phoneNo}."


class Account:

    # def __init__(self, *args):
    #     if len(args) == 0:
    #         self.customer = args[0]
    #     if len(args) == 1:
    #         self.customer = args[0]
    #         self.accountNo = args[1]
    #     elif len(args) == 2:
    #         self.customer = args[0]
    #         self.accountNo = args[1]
    #         self.balance = args[2]

    def __init__(self, customer, accountNo, balance):
        self.customer = customer
        self.accountNo = accountNo
        self.balance = balance

    def __str__(self):
        return f"This is {self.customer.name}'s account. The account number is {self.accountNo}. The balance is {self.balance}"



class Bank:

    def __init__(self, account = []):
        self.account = account

    def __str__(self):
        for accounts in self.account:
            return f"Bank Accounts: {str(accounts)}"


mada = Customer('Mada','123')
kuba = Customer('Kuba','456')
yenny = Customer('Yenny','789')

madaAccount = Account(mada, '0123', 1000)
kubaAccount = Account(kuba, '0456', 1000)
yennyAccount = Account(yenny, '0789', 1000)

keaBank = [madaAccount, kubaAccount, yennyAccount]
newBank = Bank(keaBank)
