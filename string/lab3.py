user_name = input("Enter your name:").lower()
password = input("Enter your password(password should not username ): ").lower()
n = len(user_name)
score = 100
count = 0
if user_name[:n//4] in password :
    score = score - len(user_name[:n//4])*2
    print(f"Your score is {score}, because  you have {user_name[:n//4]} in your username ")
if user_name[:n//2] in password :
    score = score - len(user_name[:n//2])*4
if user_name[:-1] in password :
    print(user_name[:-1])
    score = score - len(user_name[:-1])*5
if score > 80:
    print("your password is strong ")
elif  score < 80 and score > 50 :
    print("your password is moderate level  ")
else:
    print("your password is weak")





