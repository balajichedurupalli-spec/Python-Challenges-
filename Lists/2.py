
n = int(input("enter the number of students:"))
student_ids = [-1] * n
for i in range(n):
    student_ids[i] = int(input("enter the student ID :"))
for i, id in enumerate(student_ids):
    print(f" {i}  : {id }")

new = int(input("enter the student ID :"))
loc = int(input("enter the location to insert new student :"))


if loc < 0 or loc > len(student_ids):
    print("invalid location")
else:
    student_ids += [0]

    n = len(student_ids)

    for i in range(n-1, loc, -1):
        student_ids[i] = student_ids[i-1]

    student_ids[loc] = new

print(student_ids)





