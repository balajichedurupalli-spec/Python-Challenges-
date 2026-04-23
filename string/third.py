email = input("enter your email:")
if "@" in email and "." in email and "@" != email[0]:
    print("email is valid")
else:
    print("email is not valid")
