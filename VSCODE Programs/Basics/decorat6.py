#Args and kwrargs are used for multiple arguments and parameters.
def star(func):
    def inner(*args,**kwrargs):
        print("*"*30)#1
        func(*args,**kwrargs)
        print("*"*30)#5
    return inner
def percent(func):
    def inner(*args,**kwrargs):
        print("%"*30)#2
        func(*args,**kwrargs)
        print("%"*30)#4
    return inner
@star
@percent
def printer(msg):
    print(msg)

printer("           Kandarp            ")#3
printer("           Manish             ")