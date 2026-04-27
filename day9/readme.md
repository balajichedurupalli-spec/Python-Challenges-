# Smart Inventory Mutation Tracker
## Scenario
This project simulates a warehouse inventory system to analyze the risks of data duplication. By using Shallow and Deep copying, the system tracks how nested modifications (like price discounts or stock updates) can unintentionally corrupt original records due to memory reference sharing.

## Features
Nested Data Structure: Manages inventory items with sub-dictionaries containing price, stock, and supplier_rating.

Copy Integrity Analysis: Demonstrates the difference between reference-based (shallow) and value-based (deep) duplication.

Automated Mutation: Applies a 10% discount and stock reduction to targeted items.

Reference Leak Detection: Identifies which copy operation failed to isolate the master data from changes.

## Requirements
Python 3.x

copy module (Standard Library)

## Personalization (Roll Number: 24110011667)
Mutation Rule: 24110011667(mod3)=1.

Target: Only the item at Index 1 (Phone) is modified in the copied datasets.

Threshold Logic: A "Rating Boost" of +0.5 is applied to the mutated item to observe if metadata also leaks back to the original inventory.

## Why Shallow Copy Fails
In this implementation, the inventory is a list of dictionaries. A Shallow Copy (copy.copy) creates a new list, but the internal details dictionaries are not duplicated—they are simply referenced.

When the price is modified in the shallow copy, the change "leaks" back to the original inventory because both objects point to the same memory location for the details dictionary. Only Deep Copy ensures total data isolation.

## Expected Output
Original Inventory: Shows changes if a shallow copy was mutated (Leakage).

Shallow Copy Result: Shows the mutated values.

Deep Copy Result: Shows independent mutated values.

Summary Tuple: (Changed_Items_Count, Unchanged_Items_Count)