

class Atm(object):
    def __init__(self, Atm_card_number, Atm_Pin):
        self.Atm_card_number=Atm_card_number
        self.Atm_Pin=Atm_Pin
        
        
    def BalanceEnquiry(self):
        return("You have the total balance of 100$ left. ")

    def CashWithdrawl(self):
        amount=int(input("How much do you want to withdraw: "))
        balance=100-amount
        return(f"You succesfully withdrawed {amount}! You now have left {balance}.")

 


    
user=Atm(211,53)
print(user.BalanceEnquiry())
print(user.CashWithdrawl())
