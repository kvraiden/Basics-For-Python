def calli():
    def reti():
        for x in range(0,20):
            print("+")
        print("Inside reti which is subfunction of calli......")
    return reti
nop = calli()
nop()