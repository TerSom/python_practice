try:
    users = open("users.txt", "r")
    list = users.readlines()

    print(list[1])

    index = 1
    for user in list:
        print(f"{index} - {user}")
        index += 1

    users.close()

except:
    print("file tidak ditemukan")