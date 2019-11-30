year=int(input("enter the number"))
if(year%400!=0):
    if(year%100!=0):
        if(year%4!=0):
            print("not leap year")
else:
    print("leap yaer")
    
