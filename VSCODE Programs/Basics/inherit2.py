class polygon:
    def __init__(self,noofsides): #Main init function
        self.n = noofsides
        self.sides=[]
        for i in range(noofsides):
            self.sides.append(i)
    def input_sides(self):#Taking sides by iterating using for loop
        for i in range(self.n):
            self.sides[i]= float(input("Enter side:"))
    def display_sides(self):
        for i in range(self.n):#Displaying sides by using the for loop again
            print("Side",i+1,"is",self.sides[i])

p1 = polygon(3)
p1.input_sides()
p1.display_sides()

#Complexity of the program: O(n+n+n) because sequential statements
#At last it depends on the n so O(n)