prices = ( 200, 250 , 300 , 350 , 500)
print("Prices: ", prices)
Max = prices[0]
for i in range(1,len(prices )):
    if prices[i] > Max :
        Max = prices[i]
print("Maximum price in tuple :", Max )
