temperatures = (40 , 30 , 50 , 65  )
print("Temperatures: ", temperatures)
Max = temperatures[0]
for i in range(len(temperatures)):
    if temperatures[i] > Max:
        Max = temperatures[i]
print("Maximum recorded temperature: ", Max, "celsius")
