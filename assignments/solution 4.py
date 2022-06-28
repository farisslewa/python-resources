class bank_info():
  def __init__(self,owner,balance):
    self.owner = owner
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount
    print(f"you made a deposit of {amount}$, your current balance is {self.balance}$")
  def withdraw(self,amount):
    if amount > self.balance :
      print(f"you can not make withdraw of {amount}$, becuase you don't have enough balance, your current balance is {self.balance}$ ")
    else:
      self.balance -= amount
      print(f"you made a withdraw of {amount}$, your current balance is {self.balance}$")
  def __str__(self):
    return f'{self.owner} have {self.balance}$'

Faris = bank_info('Faris',1000)
Faris.deposit(150)
Faris.withdraw(100)
print(Faris)