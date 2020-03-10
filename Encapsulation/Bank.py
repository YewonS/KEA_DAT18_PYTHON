class Bank:
    def __init__(self):
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts
    
    @accounts.setter
    def accounts(self, account):
        self.__accounts.append(account)

class Account:
    def __init__(self, accountNo, customer):
        self.accountNo = accountNo
        self.customer = customer

class Customer:
    def __init__(self, name, age):
        if(age >= 18):
            self.name = name
        else:
            print("You cannot create a bank account yet. Grow old and come back.")

