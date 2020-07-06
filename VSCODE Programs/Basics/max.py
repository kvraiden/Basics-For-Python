num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the sec number: "))
num3 = int(input("Enter the third num:"))

#Logic

if num1>num2 and num1>num3:
    print("Max number is :", num1)
elif num2>num1 and num2>num3:
    print("Max number is :", num2)
else:
    print("Max number is :", num3)