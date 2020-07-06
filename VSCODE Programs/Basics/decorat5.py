def makerpr(func):
    def inner():
        print("New facelifted model...")
        
    return inner

@makerpr#Another simple way to use decorater syntax @Functionname without parenthesis
def ord():
    print("I am old model...")


ord()

