# Python-Challenges-

# Day 1 Python Project

##  Project Description
This project contains the Python code I wrote on **Day 1** while learning Python.  
It’s mainly about getting comfortable with the basics — understanding syntax, writing simple logic, and seeing how things actually work in code.

This is the starting point of my Python learning journey and sets the foundation for more advanced topics ahead.

---

##  Features
- Simple and easy-to-read Python code  
- Focuses on Python basics  
- Beginner-friendly and great for practice  
- Easy to tweak and experiment with  

---

##  Technologies Used
- Python 3

---

## Notes
- Feel free to play around with the code and try your own ideas.
- This project is meant for learning, not perfection 

-----------------------------------------------------



#  Day 2 Python Project

## Smart ID & Credential Validator

## Overview
Validates student registration details using **only strings and conditional statements**.  
Checks Student ID, Email, Password, and Referral Code.

## Validation Rules
- **Student ID:** Format `CSE-XXX`, last 3 digits must be numbers  
- **Email:** Must contain `@` and `.`, cannot start/end with `@`, ends with `.edu`  
- **Password:** Min 8 chars, first letter uppercase, at least one digit  
- **Referral Code:** Format `REF##@`, last two digits numbers, ends with `@`

## Approach
- Inputs are strings  
- Conditions check validity using indexing and comparisons  
- Boolean variable tracks overall validity  
- Prints `Approved` if all pass, else `Rejected`

## Learning Outcome
- Learned string validation using conditions  
- Practiced indexing, slicing, and logical checks without loops or regex

#  Day 3 Python Project 

## Student Performance Analyzer
## Overview

Analyzes student marks and classifies performance using basic Python concepts like lists, loops, and conditional statements.

## Classification Rules

90 – 100 → Excellent

75 – 89 → Very Good

60 – 74 → Good

40 – 59 → Average

0 – 39 → Bad

< 0 or > 100 → Invalid

## Approach

Marks are stored in a list

A for loop processes each mark

Conditional statements classify performance

Counters track valid and failed students

Personalized logic uses register number parity

## Personalization

If the register number is even and marks ≥ 90, output shows:
Excellent (consistent performance)

## Learning Outcome

Learned how to process lists using loops, apply conditional logic, validate inputs, and implement personalized conditions without using built-in functions or advanced data structures.
