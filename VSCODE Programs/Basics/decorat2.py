#Higher order function
def inc(x):
    return x + 1
    
def dec(x):
    return x - 1

def opr(func,x):
    res = func(x)
    return res

count = 0
for i in range(0,10):
    print(opr(inc,10))
    count = count+1
print(count)#Returns loop count


print(opr(dec,10))#Simply decrements the 10 to 9