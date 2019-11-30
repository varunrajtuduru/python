number=int(input("enter the number"))
count=0
factors=[]
for i in range(1,number+1):
    
    if(number%i==0):
        count=count+1
        factors.append(i)
print(count)
print(factors)
print(sum(factors))

