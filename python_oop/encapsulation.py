class BankAccount:
    __no = ""
    __belance = 0

    def __init__(self,no):
        self.__no = no

    @property
    def belace(self):
        return self.__belance
    
    @property
    def no(self):
        return self.__no
    
    def topup(self,amount):
        self.__belance += amount

    def cashout(self,amount):
        if amount > self.__belance:
            raise ValueError("saldo anda tidak cukup")
        self.__belance -= amount

terry_account = BankAccount("kocak")
print(terry_account.no)
terry_account.topup(10000) 
print(terry_account.belace)
terry_account.cashout(2000)
print(terry_account.belace) 

