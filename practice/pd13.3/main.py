class BankAccount:
    int_rate=2
    min_balance=100
    def __add__(self, other):
        if type(other)in [int,float]:
            self.balance+=other
    def __del__(self):
        print(self,'is deleted')
    def __str__(self):
        return self.name+' '+self.ac_no
    def __init__(self,name,balance,ac_no):                      # print('object created')
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
# ram+10
# print(ram.balance)
del ram
print(ram.balance)
