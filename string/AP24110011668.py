from wsgiref.validate import validator

price =[100,200,0,300,400,600]
count = 0
for i in range(len(price)):
    if price[i] > 0:
        print("valid price")
        count =count+1
    elif price[i] <=0:
        print("invalid price")
    else:
        print("not eligible")
print("number of  valid price is:",count)
