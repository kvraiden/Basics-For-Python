class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass
    
num = 10

while True:
    try:
        i_num = int(input("Enter a number:"))
        if i_num<num:
            raise ValueTooSmallError
        elif i_num>num:
            raise ValueTooLargeError
        elif i_num==num:
            print("U r right.")
            break

    except ValueTooSmallError:
        print("This is too small.")
    except ValueTooLargeError:
        print("This is too large.")
      