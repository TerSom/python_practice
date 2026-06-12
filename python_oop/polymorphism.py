class Hewan:
    def __init__(self,name):
        self.name = name

    def suara(self):
        return "hewan bersuara"
    

class Anjing(Hewan):
    def suara(self):
        return "Guk Guk!"
    
class Kucing(Hewan):
    def suara(self):
        return "Meow Meow!"

class Sapi(Hewan):
    def suara(self):
        return "Mooo!"
    
hewan_list = [
    Anjing("budi"),
    Kucing("terry"),
    Sapi("umay")
]

for hewan in hewan_list:
    print(hewan.suara())

class Mobil:
    def start(self):
        print("mesin mobil di nyalakan")

class Motor:
    def start(self):
        print("mesin motor di nyalakan")

class Perahu:
    def start(self):
        print("mesin perahu di nyalakan")

def operasikan_kendaraan(kendaraan):
    kendaraan.start()

kendaraan_list = [
    Mobil(),
    Motor(),
    Perahu()
]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)

class Apple:
    def __init__(self,jumlah):
        self.jumlah = jumlah
    
    def __add__(self, other):
        return Apple(self.jumlah + other.jumlah)

    def __str__(self):
        return f"apple: {self.jumlah}"
    

apple1 = Apple(10)
apple2 = Apple(10)
apple3 = apple1 + apple2
print(apple3)

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width
    
class Cricle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
shape = [
    Rectangle(5,3),
    Cricle(18)
]

for s in shape:
    print(f"Area is {s.area()}")