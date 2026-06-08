class Kampus:
    nama = ""
    alamat = ""

class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"halo nama saya {self.nama}")

kampus1 = Kampus()
print(kampus1.nama)
print(kampus1.alamat)

kampus2 = Kampus()

print(type(kampus1))
print(type(kampus2))

Mahasiswa1 = Mahasiswa()
Mahasiswa1.nim = 123
Mahasiswa1.nama = "kocak"
Mahasiswa1.perkenalan()

print(Mahasiswa1.nim)
print(Mahasiswa1.nama)

Mahasiswa2 = Mahasiswa()
Mahasiswa2.nim = 321
Mahasiswa2.nama = "umay"
Mahasiswa2.perkenalan()

print(Mahasiswa2.nim)
print(Mahasiswa2.nama)

print(type(Mahasiswa1))
print(type(Mahasiswa2))