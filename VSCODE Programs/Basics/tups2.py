#Changing elements of tuple
#lists in tuple can be changed
#Not the single elements

tipu = (1,2,3,[4,5,5])
tipu[3][1] = 100
print(tipu)
print(tipu+(4,5,6))
print(tipu*2)
res = tipu.index(2)
print(res)

#del tipu
#print(tipu)