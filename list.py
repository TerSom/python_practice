# names = ["darman","umay","terry","gg gaming","kocak"]

# for name in names:
#     print(f"nama : {name}")

# numbers = [5,6,7,8,1]

# numbers.append(99)
# print(numbers)

# numbers.insert(2,100)
# print(numbers)

# numbers.pop(5)
# print(numbers)

# numbers.remove(8)
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers = [5, 6, 7, 8, 1]

# init_number = 0
# for number in numbers:
#     init_number = init_number + number

# print(init_number)

numbers = [5, 6, 7, 8, 1]

# total = sum(numbers)
# print(total)

# max_number = max(numbers)
# print(max_number)

# numbers.sort()
# angka_terbesar = numbers[-1]
# print(angka_terbesar)

max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)