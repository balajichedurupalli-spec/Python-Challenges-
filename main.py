from math import sqrt
nums = [11, 22 , 13, 44, 17 , 28 , 19 ]
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i != 0:
            continue
        else:
            return False
    return True
def f(nums):
    arr = []
    for num in nums:
        if num % 2 != 0 and is_prime(num):
            continue
        else:
            arr.append(num*2)
    arr.sort()
    return arr[-3:]
print(f(nums))
