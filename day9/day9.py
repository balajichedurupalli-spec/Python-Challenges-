import copy
def create_inventory():
    return [
        {"item": "Laptop", "details": {"price": 50000, "stock": 10, "supplier_rating": 4.5}},
        {"item": "Phone", "details": {"price": 20000, "stock": 25, "supplier_rating": 4.2}},
        {"item": "Tablet", "details": {"price": 30000, "stock": 15, "supplier_rating": 4.0}}
    ]

def apply_discount(data, roll_mod):
    # rule: modify only index matches 24110011667 % 3 = 1
    for i in range(len(data)):
        if i == roll_mod: 
            data[i]["details"]["price"] *= 0.9
            data[i]["details"]["stock"] -= 5
            data[i]["details"]["supplier_rating"] = min(5.0, data[i]["details"]["supplier_rating"] + 0.5)
    return data
def compare_data(original, modified):
    print("\n--- Structural Comparison ---")
    changes = 0
    stable = 0
    for i in range(len(original)):
        
        if original[i]["details"] is modified[i]["details"]:
            print(f"Index {i} ({original[i]['item']}): REFERENCE LEAK DETECTED")
            changes += 1
        else:
            print(f"Index {i} ({original[i]['item']}): INDEPENDENT")
            stable += 1
    return (changes, stable)
ROLL_NUMBER = 24110011667
inventory = create_inventory()
MOD_INDEX = ROLL_NUMBER % len(inventory) 

shallow_inv = copy.copy(inventory)
deep_inv = copy.deepcopy(inventory)
apply_discount(shallow_inv, MOD_INDEX)

print("original inventory (after shallow mutation ):")
for item in inventory: print(item)
print("\nshallow copy results:")
for item in shallow_inv:
    print(item)
print("\ndeep copy results :")
for item in deep_inv:
    print(item)
summary = compare_data(inventory, deep_inv)
print(f"\nfinal summary tuple (leaked , independent): {summary}")