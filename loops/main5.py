salaries = (1000, 3999 ,4000, 5000, 10000 )
print("Salaries :",salaries)
total_payout = 0

for i in range(len(salaries) ) :
    total_payout += salaries[i]

print("Total payout :",total_payout)