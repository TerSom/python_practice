while True:
    operator = input("masukan operator (+,-,*,//,**,%) : ")
    
    # exit
    if operator == "exit":
        break

    # is_operator?
    if operator not in ("+","-","*","//","**","%"):
        print("masukan operator yang benar!!!")
        continue


    # is_number?
    try:
        angka_pertama = int(input("masukan angka pertama : "))
        angka_kedua = int(input("masukan angka pertama : "))
    except:
        print("masukan angka!!!")
        continue
        
    # operator
    if operator == "+":
        jumlah = angka_pertama + angka_kedua
        print(jumlah)
    elif operator == "-":
        jumlah = angka_pertama - angka_kedua
        print(jumlah)
    elif operator == "*":
        jumlah = angka_pertama * angka_kedua
        print(jumlah)
    elif operator == "//":
        jumlah = angka_pertama // angka_kedua
        print(jumlah)
    elif operator == "**":
        jumlah = angka_pertama ** angka_kedua
        print(jumlah)
    elif operator == "%":
        jumlah = angka_pertama % angka_kedua
        print(jumlah)

    is_done = input("mau lanjut (y/n) : ")
    if is_done == "y":
        continue
    else:
        print("terima kasih sudah bermain")
        break

