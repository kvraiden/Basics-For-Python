n = int(input("Enter the number: "))
def calc_sum(n):
    if n==1:
        return 1
    else:
        return n+calc_sum(n-1)
sum = calc_sum(n)
print(sum)