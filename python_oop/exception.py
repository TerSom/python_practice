class BelanceNotEnough(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class BankAccount:
    def __init__(self, no, balance =0):
        self.no = no
        self.balance = balance

    def tranfer(self,amount):
        if amount > self.balance:
            raise BelanceNotEnough("saldo tidak mencukupi")
        self.balance -= amount

try:
    terry_account = BankAccount("24242242", 100)
    terry_account.tranfer(100000)
except BelanceNotEnough as e:
    print(f"error : {e}")

print("programn selesai")