units = int(input("Please enter number of units: "))
if units <= 100 and units >= 0:
    print(f"you have used {units} units . Total amount is {(units * 1.5) +50}")
elif units <= 200 and units > 100:
    print(f"you have used {units} units . Total amount is {(units * 2.5) +50}")
elif units <= 300 and units > 200:
    print(f"you have used {units} units . Total amount is {(units * 3.5) +50}")
elif units > 300 :
    print(f"you have used {units} units . Total amount is {(units * 6.0) + 50}")
