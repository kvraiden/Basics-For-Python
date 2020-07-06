#Set is an unordered collection of item
#It uses {} as a symbol
#it can contain multiple datatypes
# Two examples are given below
#Automatically removes duplicate

my_s = {1,1,2,3}
print(my_s)
my_s1 = set([1,5,2,5,4])
print(my_s1)
my_s1.add(6)#add will only add 1 arument
print(my_s1)
my_s1.update([111,75,45,97])#Adds multiple elements as a list
print(my_s1)