#Nonlocal variables inside nested functions
def print_msg(msg):
    def prinbr():
        print(msg)
    return prinbr
    prinbr()

a = print_msg("Dayumm")
a()

del print_msg#Even after deleting we can see the result printed
a()