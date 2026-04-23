username = input("Please enter your username: ")
password = input("Please enter your password:")
if username == " " or len(password) < 8:
    print("login failed")
else:
    print("login successful")

