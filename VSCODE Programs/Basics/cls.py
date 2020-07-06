class My_Sec:
    a = 0
    def funt(self):
        return 'Fine'

ob1 = My_Sec()
ob2 = My_Sec()

print(ob1.a)
print(ob2.a)

ob1.a = 1000
ob2.a = 500

print(ob1.a)
print(ob2.a)
print(ob1.funt())

#Now using class as an object
print(My_Sec.a)