user_name = input("Please enter your username: ")
password = input("Please enter your password: ")
if user_name == "Balaji123" and password != "12345":
    print("please enter a valid password")
elif user_name != "Balaji123" or password == "12345":
    print("please enter valid username")
elif user_name == "Balaji123" and password == "12345":
    print("welcome Balaji123")



