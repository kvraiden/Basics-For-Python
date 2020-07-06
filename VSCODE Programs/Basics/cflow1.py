n = int(input("Enter the number to check odd or even: "))
try:
        if n%2==0:
            print("It's Even.")
        elif n==0:
            print("Zero.")
        else:
            print("It's Odd.")
        if n=="exit":
            exit
except ValueError:
    print("Enter valid input.")