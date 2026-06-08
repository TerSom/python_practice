import random

answer = random.randint(1,10)
trying = 0
limit = 3

while True:
    gues_number = int(input("masukan angka dari 1-10 : "))
    trying += 1

    if gues_number == answer:
        print(f"selamat kamu menang jawabanya adalah {answer}")
        break
    elif trying == limit:
        print(f"kamu kalah jawabanya adalah {answer} ayo coba lagi")
        break
