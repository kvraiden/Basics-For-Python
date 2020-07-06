#Program for fibonacci series
n_term = int(input("Enter the last term of your series."))

n1 = 0
n2 = 1
count = 0

print("Fibonacci series upto",n_term,":")
while count<n_term:
    print(n1,end=", ")
    nth = n1 + n2
    n1=n2
    n2=nth
    count += 1
print()
