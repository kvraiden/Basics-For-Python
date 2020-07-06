#Lambda means anonymous function
#Syntax is (lambda arguments: expression)
n = int(input("Enter the num:"))

square = lambda x:x*x

result = square(n)
print(result)
