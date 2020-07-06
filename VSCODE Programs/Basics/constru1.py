#Program to find distance between (0,0)and other axis
class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def distance(self):
        return (self.x**2+self.y**2)

p1 = Point(6,8)
distance = p1.distance()
print(distance)

