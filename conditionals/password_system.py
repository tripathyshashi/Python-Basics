username = input("Enter username : ")
password = input("Enter password : ")
if (username=="admin" and password=="pass"):
    print("LOGIN successful")
elif (username != "admin"):
    print("Wrong username")
else:
    print("Wrong password")


