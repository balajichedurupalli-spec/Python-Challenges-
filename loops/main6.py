marks = [20, 40 , 48 , 83, 95 ]
for i in range(len(marks)):
    if marks[i] >= 40 :
        print(i+1 , " : ", marks[i] , "Status : PASS")
    else:
        print(i+1 , " : ", marks[i] , "Status : FAIL")