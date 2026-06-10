class Mahasiswa:
    nim = 0
    nama = "" 

    def __init__(self,nim,nama):
        self.nim = nim
        self.nama = nama
    
    def __str__(self):
        return f"mahasiswa : {self.nim} - {self.nama}"
    
    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama
    
    def __lt__(self, other):
        return self.nim < other.nim
    
    def __gt__(self, other):
        return self.nim > other.nim
    
    def __le__(self, other):
        return self.nim <= other.nim
    
    def __ge__(self, other):
        return self.nim >= other.nim

mhs = Mahasiswa(2000200,"terry")
mhs2 = Mahasiswa(200000,"terry")

print(mhs.nim)
print(mhs.nama)

print(f"{mhs}")

print(mhs >= mhs2)

# class BankAccount:
#     no = ""
#     saldo = 0

#     def __init__(self,no,saldo):
#         if saldo < 0:
#             raise ValueError("saldo harus positif")


#         self.no = no
#         self.saldo = saldo

# terry = BankAccount("111231113",2131231)
# somay = BankAccount("423423",-1)