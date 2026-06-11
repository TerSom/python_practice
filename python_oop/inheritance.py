class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Merk {self.merk} tahun {self.tahun}"
    
    def nyalakan(self):
        print(f"{self.merk} dinyalakan")

class Mobil(Kendaraan):

    def __init__(self,merk,tahun,jumlah_roda):
        super().__init__(merk,tahun)
        self.jumlah_roda = jumlah_roda

    def klakson(self):
        print(f"Mobil {self.info()} klakson")

# porshce = Mobil("gt3 rs",2023,4)
# print(porshce.info())
# porshce.nyalakan()
# porshce.klakson()


class Motor(Kendaraan):

    def klakson(self):
        print(f"motor {self.info()} klakson")
    
    def nyalakan(self):
        print(f"motor {self.merk} dinyalakan otomatis")

ducati = Motor("panigale",2024)
print(ducati.info())
ducati.nyalakan()
ducati.klakson()

class Karyawan:
    def __init__(self, name, gaji):
        self.name = name
        self.gaji = gaji

class Karawantetap(Karyawan):
    pass

class Manager(Karawantetap):
    pass

class VoicePresident(Manager):
    pass

class BisaBerlari:
    def berlari(self):
        print("berlarii sangat cepat")

class BisaBerenang:
    def berenang(self):
        print("Berenang sangat cepat")

class Atlit(BisaBerenang,BisaBerlari):
    def __init__(self,name):
        self.name = name

terry = Atlit("terry")
terry.berenang()
terry.berlari()

class A:
    def method(self):
        print("Metrhod from A")

class B(A):
    def method(self):
        print("Metrhod from B")

class C(A):
    def method(self):
        print("Metrhod from C")

class D(B,C):
    pass

d = D()
d.method()


terry = Karyawan("terry",1313)
terry2 = Karawantetap("terry2",1313)
terry3 = Manager("terry2",1313)
terry4 = VoicePresident("terry2",1313)

print(isinstance(terry,Karyawan))
print(isinstance(terry2,Karyawan))
print(isinstance(terry3,Karyawan))
print(isinstance(terry4,Karyawan))S