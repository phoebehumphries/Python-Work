num1 = input("enter number: ")
num2 = int(num1)
binary = ""
while num2 != 0:
    binary = str(num2 % 2) + binary
    num2 //= 2
    print(binary)

num = int(input("Please enter a number: "))
print(bin(num)[2:])

num = int
binary_num = ''
binary_num = str(binary_num)

# another try...

num = int
binary_num = ''
binary_num = str(binary_num)
num = input("Please enter the number you want to convert!")
while num != 0:
    binary_num = str(num % 2)

print(binary_num)
print()
