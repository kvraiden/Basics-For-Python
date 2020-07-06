#We will use generator function to find reverse of a string.
#Here advanced slicing is used which is helpful in any kind of string programs
#[start,stop,step]
my_str = str(input("Enter the string: "))
def rev_str(my_str):
    lenth = len(my_str)
    for i in range(lenth-1,-1,-1):#Starts at secondlast pos,saves that char in yield,again decreases the size 
        yield my_str[i]
    
for char in rev_str(my_str):
    print(char,end='')
print()


