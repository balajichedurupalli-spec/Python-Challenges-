student_id = input("enter student ID :")
email = input("enter email :")
password = input("enter password :")
refferal = input("enter refferal:")

valid = True
# student_id
if len(student_id) != 7:
    valid = False
elif student_id[0:3] != "CSE":
    valid = False
elif student_id[3] != "-":
    valid = False
elif not (student_id[4].isdigit() and student_id[5].isdigit() and student_id[6].isdigit()):
    valid = False

# email
if "@" not in email or "." not in email:
    valid = False
elif email[0] == "@" or email[-1] == "@":
    valid = False
elif email[-4:] != ".edu":
    valid = False

# password 
if len(password) < 8:
    valid = False
elif not ('A' <= password[0] <= 'Z'):
    valid = False
elif not (
    password[1].isdigit() or password[2].isdigit() or password[3].isdigit() or password[4].isdigit() or
    password[5].isdigit() or password[6].isdigit() or password[7].isdigit()
):
    valid = False



# refferal
if len(refferal) != 6:
    valid = False
elif refferal[0:3] != "REF":
    valid = False
elif not (refferal[3].isdigit() and refferal[4].isdigit()):
    valid = False
elif refferal[5] != "@":
    valid = False


if valid:
    print("Approved !!")
else:
    print("Rejected!!")


    
