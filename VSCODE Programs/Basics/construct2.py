#Deleting an object
class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

p1 = Point(1,2)
print((p1.x,p1.y))

del p1.y

print(p1.x)
print(p1.y)#It must show an error