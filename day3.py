register_no = int(input("Enter your register number (last 3 digits : ):"))

n = int(input("Enter  no  of  elements  :"))
marks = [0] * n
for i in range(n):
    num = int(input(f"enter marks  {i} : "))
    marks[i] = num

Valid_count = 0
fail_count = 0

for mark in marks :

    if mark < 0 or mark > 100 :
        print(f"{mark} -> Invalid")

    else:
        Valid_count += 1

        # persionalized
        if mark >= 90 :

            if  register_no % 2 == 0:
                print(f"{mark} -> Excellent ( consistent performance )")
            else:
                print(f"{mark} -> Excellent")


        elif mark >= 75 :
            print(f"{mark} -> Very Good")

        elif mark >= 60 :
            print(f"{mark} -> Good")

        elif  mark >= 40 :
            print(f"{mark} -> Average")

        else:
            print(f"{mark} -> Bad")
            fail_count += 1


print("\nFinal Summary ")


print("\nTotal Valid Students : ", Valid_count)
print("Total Fail Students : ", fail_count)














