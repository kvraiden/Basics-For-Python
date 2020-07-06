#Program for variable scope practice

def my_fun():
    x =  10
    print("Value inside the scope:",x)

x = 20
my_fun()
print("Value outside the scope",x)
