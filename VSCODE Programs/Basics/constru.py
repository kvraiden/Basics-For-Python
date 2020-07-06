#__DoubleUnderscore means we have a special function
#We need to focus on __init__(You might have seen it multiple times)
#These are also known as constructors
class My_Third:
    def __init__(self,p1=0,p2=0):
        self.a = p1
        self.b = p2
obj1 = My_Third(5,6)
obj2 = My_Third()
print((obj1.a,obj1.b))#Here we passed values of a and b as a parameter
print((obj2.a,obj2.b))#We did not pass the value pf a and b so it takes default assigned value
