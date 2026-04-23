username = input("Enter your username: ")
if len(username) < 5 or  username.count(" ")!=0 :
    print("invalid username")
else:
    print("valid username")
