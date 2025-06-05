
class Bankaccount :

    def __init__ (self , account_number , holder_name,initial_balance=0):


      self .account_number = account_number
      self .holder_name = holder_name
      self .balance = initial_balance



    def deposit (self,amount):

        if amount > 0:
            self .balance += amount
            print(f"Deposited ₹{amount : .2f}.  New balance is ₹ {self .balance : .2f} .")
        else:
            print ("Deposit amount must be positive.")
    def withdraw (self, amount):
        if 0 < amount <= self.balance:
            print(f"withdrew ₹{amount:.2f}. New balance is ₹ {self.balance: .2f} .")
        
        else:              
         print ("Insufficient funds or invalid amount .")

    def get_balance(self):
            return self .balance


    def __str__(self):
        return (f"Account Number {self .account_number}\n"
        f"holder Name :{self .holder_name}\n"
        f"Balance: ₹{self .balance: .2f}")


if __name__ == "__main__":
     


    Account = Bankaccount ("12345678" , "Antima" , 1000)
 
    print(Account)

    Account .deposit (300)
    Account .withdraw (400)
    Account .withdraw(10000)

    print (f" Final balance : ₹ { Account .get_balance():2f}")