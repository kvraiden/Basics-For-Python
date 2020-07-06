def makerpr(func):
    def inner():
        print("New facelifted model...")
        
    return inner
def ord():
    print("I am old model...")



pr = makerpr(ord)
pr()
