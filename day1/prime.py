number=int(input("enter the number"))
k=0
for i in range(1,number+1):
    if(number%i==0):
        k=k+1
        if(k>2):
            break
if(k>2):
    print("not a prime")
else:
    print("prime")
