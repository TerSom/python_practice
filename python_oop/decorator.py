class MateMatika:
    
    @staticmethod
    def tambah(a,b):
        return a + b
    

print(MateMatika.tambah(1,2))

class BankAccount:
    no = ""
    balance = 0
    active = True

    def __init__(self,no,balance=0):
        self.no = no
        self.balance = balance

    @classmethod
    def disabled(cls,no,balance=0):
        result = cls(no,balance)
        result.active = False
        return result

bank_accoount = BankAccount('11231313',192346194)
print(f"{bank_accoount.no}, {bank_accoount.balance}, {bank_accoount.active}")

bank_accoount2 = BankAccount.disabled("131231131",10000)
print(f"{bank_accoount2.no}, {bank_accoount2.balance}, {bank_accoount2.active}")