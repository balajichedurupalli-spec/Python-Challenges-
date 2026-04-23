numbers = input("enter the number: ")
if numbers.isdigit() and len(numbers) == 10:
    print("valid")
else:
    print("invalid")