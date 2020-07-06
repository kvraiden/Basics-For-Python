#Union 

A = {1,2,3}
B = {4,5,2}

res = A|B
print(res)

res1 = A.union(B)
print(res1)

#Intersection
res2 = A&B
print(res2)

#Set difference
res3 = A-B
print(res3)

res4 = B-A
print(res4)

#Set Symmetric difference
res5 = A^B
print(res5)

#Another methods for set manipulation are
#.add(),.update(),.remove(),.discard(),.pop(),.clear(),.union(),.symmetric_difference()