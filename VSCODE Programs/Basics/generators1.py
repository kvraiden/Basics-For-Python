#Simple Generator function
def my_gen():
    n=1
    print("This is printed first.")
    yield n

    n+=1
    print("This is printed second.")
    yield n

    n+=1
    print("This is printed third.")
    yield n

a = my_gen()#U can also iterate through a.

for item in my_gen():
    print(item)
   