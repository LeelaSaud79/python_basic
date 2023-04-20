''' PEP8:EP 8:PEP 8 is a documentation that provide various guidelines to write readable in python.It describes 
how the developer can write beautiful code
# Constructor is a function that is defined inside a function. It is also called initalizer in python.
# Any particular method which starts with double underscore and end with double underscore.intitalizatin is the one
# which is run automatically once object is created'''
class BankAccount:
    # name='ram'
    # balance=1000
    # ac_no='12356'
    int_rate=2
    min_balance=100
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
print(sita.name)
print(ram.name)
print(ram)
print(sita)
