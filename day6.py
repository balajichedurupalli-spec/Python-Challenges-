
n = int(input("enter the number of Transactions: "))
transactions = [0]*n
for i in range(n):
    transactions[i] = int(input(f"enter transaction no. {i+1} : "))


Report = {
    "normal" : [],
    "large" : [],
    "high_risk" : [],
    "invalid" : []
}

for t in transactions:
    if t <= 0 :
        Report["invalid"].append(t)
    elif 1 <= t <= 500 :
        Report["normal"].append(t)
    elif 501 <= t <= 2000:
        Report["large"].append(t)
    else :
        Report["high_risk"].append(t)

valid_transactions = [t for t in transactions if t > 0 ]

summary = (sum(valid_transactions),  len(valid_transactions))

total_val , total_count = summary
high_risk_count = len(Report["high_risk"])

frequent = total_count > 5
large_spending = total_val > 5000
suspicious = high_risk_count >= 3

if suspicious or (frequent and large_spending):
    risk = "High Risk"
elif large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"
print(f"Categorized Transactions : {Report}")
print(f"Total Value : {total_val}")
print(f"Total count : {total_count}")
print(f"Risk Classification : {risk}")






