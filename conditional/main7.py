total_bill = int(input("Please enter the total bill: "))
if total_bill >= 2000 and total_bill < 5000:
    print(f"you can get 10% of discount and total bill is : {total_bill-(total_bill*(10/100))}")
elif total_bill >= 1000 and total_bill < 2000:
    print("you can get 5% of discount ")
elif total_bill >= 5000 :
    print("you can get 15% of discount ")