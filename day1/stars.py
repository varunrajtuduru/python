number=int(input("enter the number"))
word="python"
for i in range(1,number+1):
    print("*"*i)
for i in range(number,0,-1):
    print("*"*i)
for i in range(number,0,-1):
    print(" "*i,"*"*(number-i+1))
for i in range(1,number+1):
    print(" "*i,"*"*(number-i+1))
for i in range(0,number+1):
    print(" "*(number-i)," *"*i)
for i in range(1,len(word)+1):
        print(" "*(len(word)-i),word[0:i])

        
    


