sales = (100 , 150 , 200 , 300 , 400 , 330 , 460 , 500, 550 , 600 , 700 , 450  )
print("Sales for Each month Respectively :", sales)
annualSales = 0
for i in range(len(sales)):
    annualSales += sales[i]
print("the total Annual Sales is: ", annualSales)