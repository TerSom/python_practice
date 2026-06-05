# user = {
#     "name" : "umay somay",
#     "age" : 17,
#     "is_admin" : True
# }

# user["username"] = "gg darman"
# user["name"] = "terry gg"

# temp = user.get("name")

# print(temp)

# numbers = input("masukan angka 1-9 : ")

# number_mapping = {
#     "1" : "satu",
#     "2" : "dua",
#     "3" : "tiga",
#     "4" : "empat",
#     "5" : "lima",
#     "6" : "enam",
#     "7" : "tujuh",
#     "8" : "delapan",
#     "9" : "sembilan"
# }

# output = ""

# for i in numbers :
#     terbilang = number_mapping.get(i,"undefined")

#     output = output + terbilang + " "

# print(output)

message = input(">>> ")

emoji_mapping = {
    ":)" : "😀",
    ":D" : "😁",
    ":|" : "😹"
}

words = message.split(" ")

output = ""

for i in words:
    output = output + emoji_mapping.get(i,i) + " "

print(output)