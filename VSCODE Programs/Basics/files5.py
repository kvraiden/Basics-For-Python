#Seek and tell in python
f = open("test.txt",'r',encoding='utf-8')
f.read()
print(f.tell())
f.seek(0)
print(f.read(4))

