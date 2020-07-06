def make_mul_of(n):
    def multi(x):
        return x*n
    return multi

t3 = make_mul_of(3)#Passing n
t5 = make_mul_of(5)#Passing n

print(t3(9))#Now passing value of x for multi(x) return 9*3
print(t5(10))#Now passing value of x for multi(x) return 10*5(x*n)
print(t3(85))#Now passing value of x for multi(x) return 85*3

for i in range(0,t3(10)):
    print(t3(i))