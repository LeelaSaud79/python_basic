''' Constructor is a function that is defined inside a function. It is also called initalizer in python.
Any particular method which starts with double underscore and end with double underscore.intitalizatin is the one
which is run automatically once object is created..
Destructor is also a special method that gets executed automatically when an object exit from the scope'''
class BankAccount:
    # name='ram'
    # balance=1000
    # ac_no='12356'
    int_rate=2
    min_balance=100
    def __sub__(self,other):
        if type(other) in [int,float]:
            self.balance-=other
    def __del__(self):
        print(self,'was deleted')
    def __str__(self):
        return self.name+' '+self.ac_no
    def __init__(self,name,balance,ac_no):
        # print('object created')
        self.name=name
        self.balance=balance
        self.ac_no=ac_no
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print('insufficient balance')
ram=BankAccount('ram',100,'123')
print(ram.balance)
sita=BankAccount('sita',200,'12345')
# print(sita.name)
# print(ram.name)
# print(ram)
# print(sita)
ram-10
print(ram.balance)
del ram
# print(sita.balance)
