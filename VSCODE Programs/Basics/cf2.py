#Program for finding if year is leap or not
while True:
    y = int(input("Enter the year: "))
    if(y%4)==0:
        if(y%100)==0:
            if(y%400)==0:
                print(y,"is leap year.")
            else:
                print(y,"is not a leap year.")
        else:
            print(y,"is not leap year.")
    else:
        print(y,"is not a leap year")
    
