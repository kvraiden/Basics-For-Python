import math
n1 = int(input("Enter the num1: "))
n2 = int(input("Enter the num2: "))
if n1==0:
    raise ValueError("Lmao O literally. ")

def divv(n1,n2):
    try:
        print(n1/n2)
    except ZeroDivisionError:
        print("You cannot divide with zero.")
    except ValueError:
        print("Enter proper values.")
    
        
divv(n1,n2)



