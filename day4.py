Low_risk = []
Medium_risk = []
High_risk = []
Critical_risk = []
Valid_count = 0
Invalid_count = 0
n = int(input("enter the no of Scores : "))
Input = [0] * n
for i in range(n):
    Input[i] = int(input(f"enter the Score {i}: "))

for i in range(n):
    if Input[i]  < 0:
        Invalid_count += 1

    elif  0 <= Input[i] <= 30:
        Low_risk.append(Input[i])
        Valid_count += 1
    elif 31 <= Input[i] <= 60:
        Medium_risk.append(Input[i])
        Valid_count += 1
    elif 61 <= Input[i] <= 100:
        High_risk.append(Input[i])
        Valid_count += 1
    else :
        Critical_risk.append(Input[i])
        Valid_count += 1
""" since my last digit of registration number is ODD (AP24110011667 )  
After categorization:
Remove all Critical Risk scores
Keep Low, Medium, and High
And my personal change is Displaying After Personalized Filtering  First  followed by Original(before) Personalized Filtering
"""
print(f"Input List : {Input}")
print(f"\nRegister Digit (D):{7} \n")
print("After Personalized Filtering :")
print(f"Low Risk:{Low_risk}")
print(f"Medium Risk:{Medium_risk}")
print(f"High Risk:{High_risk}")
print(f"Critical Risk:{[]}")

print("\n\nOriginal(before) Personalized Filtering: ")
print(f"Low Risk:{Low_risk}")
print(f"Medium Risk:{Medium_risk}")
print(f"High Risk:{High_risk}")
print(f"Critical Risk:{Critical_risk}")


print(f"\n\nTotal Valid Entries : {Valid_count}")
print(f"Ignored Entries : {Invalid_count}")
print(f"Removed Due to Personalization : {len(Critical_risk)} ")
Critical_risk = []



