username = input("Enter your username: ")
first_name , last_name = username.split(" ")
if username[0] == " " or username[-1] == " ":
    print("invalid username")
if first_name != " " or last_name != " ":
    print("valid username")
    print(first_name + " " + last_name)
