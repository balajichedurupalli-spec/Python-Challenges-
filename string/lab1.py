import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0 :
            return False
    return True
num = int(input("Enter a number: "))
temp = num
rev_num = 0
x = 0
print(num)
while num > 0 :


    r = num % 10
    x += r ** 3

    rev_num = rev_num*10 + r
    num  = num // 10

if x == temp :
    print(f"num is :{temp  } is a Armstrong number ")
if is_prime(rev_num):
    print(f"num is :{rev_num} is a prime number ")
else:
    print(f"num is :{rev_num} is not a prime number ")


