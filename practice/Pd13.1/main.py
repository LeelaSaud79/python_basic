# Initalization in python
class BankAccount:
    name='ram'
    balance=10000
    ac_no='123456'
    min_balance=1000
    def __str__(self):
        return self.name+' '+self.ac_no
    def __init__(self,name,balance,ac_no):
    # print(object is created)
        self.name=name
        self.balance=balance
        self.ac_no=ac_no
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print('Not sufficient balance')
ram=BankAccount('ram',100,'100000000')
print(ram.balance)
siya=BankAccount('siya',2500,'1234455')
print(siya.name)
print(ram.name)
print(ram)
print(siya)

