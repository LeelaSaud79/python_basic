# Add a method called withdraw
class BankAccount:
    name='siya'
    balance=1000
    acc_no:'112223455677887'
    interest_rate=2
    def withdraw(self,amount):
        if self.balance-amount>=100:
            self.balance-=amount
        else:
            print('sorry,balance is not enough')

