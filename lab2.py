
data = [5, 3, 5, 2, 8 , 3, 10 , 2]
# output = [25 , 64, 100]
print(data)
new_data = []
for x in data:
    if x not in new_data:
        new_data.append(x)
print(new_data)
result = map(lambda x : x**2 , filter(lambda x : x > 3, new_data))
print(list(result))
