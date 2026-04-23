list1 = [66 , 64 , 78]
count = 0
for i in range(len(list1)):
    if list1[i] >= 75 :
        count += 1
        print(i+1, " : Eligible ")
    elif list1[i] >= 65  and  list1[i] <= 74:
        print(i+1, " : Condonation")
    else:
        print(i+1 , ": Not Eligible ")
print("No of Eligible is :", count )