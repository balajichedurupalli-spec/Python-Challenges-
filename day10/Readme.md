
#Academic Data Drift & Copy Behavior Analyzer
## Scenario
A university management system frequently duplicates student academic records for research and analysis. However, improper data handling and shallow copying lead to Data Drift and Inconsistency. This project simulates these data integrity issues, analyzes statistical patterns using NumPy and Pandas, and implements a detection system to identify copy failures and critical drift.

## Features
Automated Data Generation: Generates 10-15 student records with nested scores (Internal/Assignment).

Memory Reference Analysis: Implements both shallow copy and deep copy to demonstrate Python's memory management.

Personalized Mutation: Applies mathematical transformations (e.g., sqrt) to data based on specific Register Number rules.

Statistical Drift Detection: Compares datasets using Mean, Median, and Standard Deviation to quantify divergence.

Pattern Classification: Categorizes the system state as Stable, Minor Drift, Critical Drift, or Copy Failure Detected.

## Requirements
Python 3.x

Pandas

NumPy

## Personalization Rules (Applied)
Register Number: 24110011667

Mutation Logic: 24110011667(mod3)=2. Changes are applied only to indices divisible by 2.

Drift Threshold: 7.0+2=9.0. Drift exceeding this value triggers a "Critical Drift" alert.

Manual Metric: Mean calculation is implemented via standard loops to verify algorithm accuracy without library assistance.

## Project Structure
id: Unique Student Identifier.

marks: Student Examination Marks.

attendance: Percentage of classes attended.

scores: A nested list containing [Internal, Assignment] scores.

## Key Learning: Shallow vs. Deep Copy
In this system, a Shallow Copy fails because it only copies the reference to the nested scores list. When the scores are modified in the copy, the original baseline data is unintentionally corrupted. The Deep Copy correctly duplicates all nested levels, preserving data integrity.

## Output Example
The program provides:

Original baseline DataFrame.

Comparative analysis of nested scores in different copies.

Calculated Drift value.

Statistical Tuple: (Mean, Drift, Std_Dev).

Final System Status classification.