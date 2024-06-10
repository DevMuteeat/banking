# class Account:
#     def __init__(self, account_number,account_holder,balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Deposited{amount}. New balance:{self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"withdrew {amount}. New balance:{self.balance}")

#     def transfer(self,amount,recipient):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             recipient.balance += amount
#             print(f"Transferred {amount} to {recipient.account_holder}. New balance:{self.balance}")
    
#     def view_details(self):
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance:{self.balance}")

class Account:
    #create a class for the account creation and methods, to create, you need an account name, number, type and starting balance
    def __init__(self, account_name, account_number, account_type, balance=0.0):
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    
    '''
    #demonstration on how to use getter and setter
    @property
    def balance(self):
        return self.balance
    
    @balance.setter
    def balance(self, amount):
        self.balance += amount

    '''


    #deposit function that adds to the balance
    def deposit(self, amount):
        #check if the amount is greater than 0
        if amount > 0:
            #add the amount to the balance
            self.balance += amount
        else:
            print("Amount must be greater than 0")

    #withdraw function that subtracts from the balance
    def withdraw(self, amount):
        #check if the amount is greater than 0
        if amount > 0:
            #check if the balance is greater than amount
            if self.balance >= amount:
                #subtract the amount from the balance
                self.balance -= amount
            else:
                print("Insufficient fund")
        else:
            print("Amount must be greater than 0")

    #transfer function that withdraws funds from one account and deposit to another account
    def transfer(self, deposit_acc, amount):
        #check if account exists
        if self and deposit_acc:
            #check if balance for withdrawal and transfer is more than balance
            if self.balance >= amount:
                #withdraw amount from withdrawal account
                self.withdraw(amount)
                #deposit amount to deposit account
                deposit_acc.deposit(amount)
            else:
                print("Insufficient balance")
        else:
            print("Account do not exist")
    
    def __str__(self):
        return f"{self.account_name} with account number: {self.account_number} has a balance of {self.balance}"