#Inheritance in action
#Base class polygon
class polygon:
    def __init__(self,noofsides): #Main init function
        self.n = noofsides
        self.sides=[]
        for i in range(noofsides):
            self.sides.append(0)
    def input_sides(self):#Taking sides by iterating using for loop
        for i in range(self.n):
            self.sides[i]= float(input("Enter side:"))


#Inheriting the polygon class
#In triangle
class Triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def findar(self):
        a, b, c= self.sides
        s = (a+b+c)/2                      #Herons formula
        area = (s*(s-a)*(s-b)*(s-c))**0.5  #**Means raise to here root 2 is 0.5 so raise to 0.5
        print("The area of triangle is: ",area)
    

t = Triangle()
t.input_sides()
t.findar()