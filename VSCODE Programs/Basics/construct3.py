#Deleting the object from the code
class Test(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
p1 = Test(1,2)
print((p1.x,p1.y))

del p1#As of we have deleted it will throw an error
print((p1.x,p1.y))