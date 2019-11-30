List=[{"pid":1,"name":"timex1","cost":800,"brand":"timex","catogory":"watches","rating":4,"discount":20},
      {"pid":2,"name":"casio400","cost":1200,"brand":"casio","catogory":"watches","rating":4.5,"discount":25},
      {"pid":3,"name":"bosch6","cost":24000,"brand":"bosch","catogory":"washing machine","rating":3.8,"discount":15},
      {"pid":4,"name":"whirlpool9","cost":27000,"brand":"whirlpool","catogory":"washing machine","rating":4,"discount":20},
      {"pid":5,"name":"motog2","cost":8000,"brand":"motorola","catogory":"mobiles","rating":3.5,"discount":10},
      {"pid":6,"name":"iphone11","cost":65000,"brand":"apple","catogory":"mobiles","rating":4.5,"discount":17},
      {"pid":7,"name":"mi7","cost":400,"brand":"mi","catogory":"earphones","rating":4.4,"discount":9},
      {"pid":8,"name":"zebronics3","cost":700,"brand":"zebronics","catogory":"earphones","rating":4,"discount":25}]
print("1,sortcost,2.sortcosthtol,3.sortrating,4.sortdiscount,5.sordiscounthtol")
'''
number=int(input("enter the number from 1 to 5"))

if(number==1):
    List.sort(key=lambda el:el["cost"])
elif(number==2):
    List.sort(key=lambda el:el["cost"],reverse=True)
elif(number==3):
    List.sort(key=lambda el:el["rating"])
elif(number==4):
    List.sort(key=lambda el:el["discount"])
else:
    List.sort(key=lambda el:el["discount"],reverse=True)

for i in List:
    print("{name} rs.{cost} {brand} {catogory} {rating} {discount}".format(**i))
'''
'''
print("1.brand,2.catogory,3.name")
s=int(input("enter the number you want to filter"))
if(s==1):
    st=input("enter the brand you want to filter")
    newobj=filter(lambda el:el["brand"]==st,List)
    for i in newobj:
        print('{name} {cost} {brand} {catogory} {rating} {discount}'.format(**i))
if(s==2):
    st=input("enter the catogory you want to filter")
    newobj=filter(lambda el:el["catogory"]==st,List)
    for i in newobj:
        print('{name} {cost} {brand} {catogory} {rating} {discount}'.format(**i))
if(s==3):
    st=input("enter the name you want to filter")
    newobj=filter(lambda el:el["name"]==st,List)
    for i in newobj:
        print('{name} {cost} {brand} {catogory} {rating} {discount}'.format(**i))
'''


number=int(input("enter the number from 0 to 4"))
List2=[["cost",True],["cost",False],["rating",True],["discount",True],["discount",False]]
l=List2[number]
List.sort(key=lambda el:el[l[0]],reverse=l[1])

for i in List:
    print("{name} rs.{cost} {brand} {catogory} {rating} {discount}".format(**i))

print("0.brand,1.catogory,2.name")
number2=int(input("enter the number from 0 to 2"))


string1=input("enter something for filtering")
List3=["brand","catogory","name"]
l=List3[number2]
newobj=filter(lambda el:el[l]==string1,List)
for i in newobj:
    print('{name} {cost} {brand} {catogory} {rating} {discount}'.format(**i))

