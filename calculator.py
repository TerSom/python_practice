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
        result = angka_pertama + angka_kedua
    elif operator == "-":
        result = angka_pertama - angka_kedua
    elif operator == "*":
        result = angka_pertama * angka_kedua
    elif operator == "//":
        result = angka_pertama // angka_kedua
    elif operator == "**":
        result = angka_pertama ** angka_kedua
    elif operator == "%":
        result = angka_pertama % angka_kedua
    print(f"hasilnya adalah {result}")

    # is_done?
    is_done = input("mau lanjut (y/n) : ")
    if is_done == "y":
        continue
    else:
        print("terima kasih sudah bermain")
        break

