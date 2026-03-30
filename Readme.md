# Day 6 Python Project
##Transaction Risk Analysis System
## Overview

This project analyzes financial transactions and classifies them into different risk categories using basic Python concepts such as lists, loops, dictionaries, and conditional statements.

## Classification Rules

Transaction Categories:

≤ 0 → Invalid
1 – 500 → Normal
501 – 2000 → Large

2000 → High Risk

## Risk Classification Rules
High Risk
If high-risk transactions ≥ 3
OR (total transactions > 5 AND total value > 5000)
Moderate Risk
If total transaction value > 5000
Low Risk
All other cases
## Approach
Transactions are stored in a list
A loop is used to take user input
Another loop classifies each transaction
A dictionary is used to store categorized data
List comprehension filters valid transactions
Summary metrics (total value, count) are calculated
Conditional logic determines overall risk
## Key Concepts Used
Lists
Dictionaries
Loops (for)
Conditional statements (if-elif-else)
List comprehension
Basic data analysis logic
## Personalization Logic
Detects frequent transactions (> 5)
Detects large spending behavior (> 5000 total)
Detects suspicious activity (≥ 3 high-risk transactions)
Combines these behaviors to determine final risk level
## Learning Outcome

Learned how to:

Process and categorize real-world data
Use dictionaries for structured storage
Apply multiple conditions for decision making
Implement simple risk analysis logic
Combine different conditions to derive insights
