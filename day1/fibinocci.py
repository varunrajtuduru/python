number1=int(input("enter number1"))
number2=int(input("enter number2"))
number3=number1+number2
numbers=[]
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
for i in range(0,9):
    numbers[2+i]=numbers[1+i]+numbers[i]
    numbers.append(numbers[2+i])
print(numbers)

