# # immutable
# numbers = (5,3,1,2,4)
# # tidak bisa
# numbers[0] = 10

# unpack
numbers = (1,2,3)

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

x, *a = numbers
print(x)
print(a)



