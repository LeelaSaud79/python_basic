# Create a class of bankaccount whose attributes are name, balance , acc no , interest rate.
'''class BankAccount():
    name='ram'
    balance=1000
    acc_no='12111221321'
    interest_rate=2
    def deposit(self,amt):
        self.balance+=amt
x=BankAccount()
x.deposit(5000)
y=BankAccount
print(x.balance,y.balance)'''
class student():
    name='Ram'
    age=23
x=student()
print(type(x))
y=student
print(x.name)
x.name='siya'
print(x.name)
print(y.name)
z=student
print(z.name)