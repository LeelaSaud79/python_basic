#Create a class bank account whose attributes are name,balance, acc_no and interest_rate.
#Deposit is behavior or method.self means it is the reference to the object that has called.
class BankAccount:
    name='siya'
    balance=20000
    acc_no:'112223455677887'
    interest_rate=2
    def deposit(self,amt):
        self.balance+=amt
x=BankAccount()
x.deposit(1000)
y=BankAccount()
print((x.balance,y.balance))


