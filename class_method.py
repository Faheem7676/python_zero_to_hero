class Account():
    
    def __init__(self,owner,balance=0):
        
        self.owner=owner
        self.balance=balance
        
    def deposit(self,dep_amt):
        
        self.balance=self.balance+dep_amt
        
        print(f"Added amount{dep_amt} to the balance")
        
    def withdrawal(self,wd_amt):
        
        if self.balance>=wd_amt:
            self.balance=self.balance-wd_amt
            print("Withdral Accepted")
            
        else:
            print("Sorry no enough balance")
            
    def __str__(self):
        
        return f"Owner:{self.owner}\nBalance:{self.balance}"
    
a=Account("Rahul",5000)
print(a.owner)
print(a.balance)
print(a)
a.deposit(1000)
print(a.balance)
a.withdrawal(6000)
print(a)