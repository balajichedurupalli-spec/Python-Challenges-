# Student Performance Analysis System (Day 8)

A Python-based analytical tool designed to simulate, categorize, and visualize student academic performance data. This project utilizes industry-standard libraries like Pandas, NumPy, and Seaborn to provide deep insights into student trends and system stability.

## 🚀 Features

- **Automated Data Generation**: Generates synthetic student records including IDs, marks, attendance, and assignment scores using `NumPy` and `Random`.
- **Dynamic Categorization**: Classifies students into "Top Performers," "Good," "Average," and "At Risk" based on customizable academic thresholds.
- **Statistical Analysis**:
  - Calculates mean, standard deviation, and max marks.
  - Performs correlation analysis between marks and attendance.
  - Implements a custom Performance Index using non-linear scaling (`math.sqrt`).
- **System Health Status**: Evaluates the overall academic system status (e.g., "CRITICAL ATTENTION REQUIRED") based on risk factors.
- **Visual Insights**: Generates a correlation heatmap using `Seaborn` to visualize relationship strengths between variables.

## 🛠️ Technology Stack

- **Python 3.12+**
- **Pandas**: For data manipulation and DataFrame management.
- **NumPy**: For numerical operations and vectorized calculations.
- **Matplotlib & Seaborn**: For generating high-quality statistical visualizations.
- **Math & Random**: For simulation and foundational calculations.

## 📋 Prerequisites

Ensure you have the following libraries installed:

```bash
pip install numpy pandas seaborn matplotlib
```

## 🏃 How to Run

Simply execute the main script from your terminal:

```bash
python main.py
```

## 📊 Sample Output

The system provides a comprehensive console report:

```text
Student data frame 
 student_id  marks  attendance  assignment_score  normalized_marks  performance_index
        101     69          81                44          0.771084         168.546737
        ...

 Student Categorisation : 
Top_performers : ...
At_risk : ...

 Statistical Analysis :
Mean Marks : 56.57
Standard Deviation : 27.27
Correlation Coefficient (Marks vs Attendance) : 0.35

 Academic System Status : CRITICAL ATTENTION REQUIRED
```
