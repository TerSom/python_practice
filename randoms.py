import random

users = ['kocak','kocaks','kocakss','kocaksss','kocakssss']

batas_bawah = 0
batas_atas = len(users) - 1


for i in range(5):
    random_int = random.random(batas_bawah,batas_atas)
    print(random_int)