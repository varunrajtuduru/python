di={"sachin":"123","tendulkar":"1234"}
username=input("enter user name")
try:
    if username not in di.keys():
        raise Exception("invalid username")
except Exception as e:
    print("generic handler",e)
if username in di.keys(): 
    password=input("enter password")
    try:
        if password != di[username]:
            raise Exception("invalid password")
    except Exception as e:
        print("generic handler",e)
    
