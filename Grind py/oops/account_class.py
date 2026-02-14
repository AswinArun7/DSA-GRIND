# Create Account class with 2 attributes - balance and account number.
# Create methods for debit, credit and display balance.& printing balanace.

class Account:
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.account_no=acc_no

    def debit(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def credit(self,amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance

s1=Account(10000, 12345)      
print(s1.balance)
print(s1.account_no) 
s1.debit(5000)
s1.credit(2000) 