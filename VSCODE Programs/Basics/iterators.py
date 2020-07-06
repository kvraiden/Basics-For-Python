#Yiou can also use for loop for this same task 
my_list = [1,2,3]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())

#Uncommenting this will result in error ->: next(my_iter)
