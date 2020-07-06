sum = 0
while True:
    n = float(input("Enter the number: "))
    if n<0:
        print("Sorry the number is negative.\n")
        break
    else:
        sum +=n
        print("The Sum is : ", sum)