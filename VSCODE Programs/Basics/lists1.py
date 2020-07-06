#Changing the lists items

lis = [1,2,3,4,5]
lis[0]=10
print(lis)

lis[1:4] = [11,12,13]
print(lis)
lis.append("a")
print(lis)

lis.extend([87,545,55,44])
print(lis)

print(lis+[100])
print(['k','a']*2)

print("__________________________")
lis.insert(1,69)
print(lis)
print("__________________________")
lis[2:2] = [5,7]#Inserting at particular place
print(lis)