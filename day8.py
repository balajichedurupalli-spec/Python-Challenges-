
import numpy as np 
import pandas as pd 
import random 
import math 
import seaborn as sns 
import matplotlib.pyplot as plt

def generate_data(num_records):
    """Generate student data using random , list and tuple"""
    data = []
    student_ids = np.arange(101, 101 + num_records)
    
    for student_id in student_ids:
        marks = random.randint(0,100)
        attendance = random.randint(0,100)
        assignment_score = random.randint(0,50 )
        data.append((student_id,marks,attendance,assignment_score))
    return data 
def classify_data(df):
    """Classify each student into categories using dict {}"""
    categories = {
        "Top_performers":[],
        "Good":[],
        "Average":[],
        "At_risk":[]
    }
    for _, row in df.iterrows():
        marks , attendance = row['marks'] , row['attendance']
        if marks > 90 and attendance > 80:
            categories['Top_performers'].append(int(row['student_id']))
        elif 71 <= marks <= 90:
            categories['Good'].append(int(row['student_id']))
        elif 40 <= marks <= 70:
            categories['Average'].append(int(row['student_id']))
        elif marks < 40 or attendance < 50 :
            categories['At_risk'].append(int(row['student_id']))
    return categories
def analyze_data(df):
    """ performing numerical analysis using numpy ,  manual calculations  and  plotting graphs using seaborn """
    marks = df['marks'].values
    # mean manual 
    mean = sum(marks)/len(marks)
    # numpy 
    std_dev = np.std(marks)
    max_marks = np.max(marks)
    min_marks = np.min(marks)
    correlation = np.corrcoef(df['marks'],df['attendance'])[0, 1]
     
    diff = max_marks - min_marks
    df['normalized_marks'] = [(m-min_marks)/diff if diff != 0 else 0.0 for m in marks ]

    # performance index 
    
    df['performance_index'] = df.apply(lambda r : (math.sqrt(r['marks']* r['attendance'])+r['assignment_score']**1.2), axis=1)

    return {
        'stats' : (mean,std_dev,max_marks),
        'correlation' : correlation
    }

num_records = 7 ## since last digit of registration No AP24110011667 is 7 
data = generate_data(num_records)

columns = ['student_id','marks','attendance','assignment_score']
df = pd.DataFrame(data, columns = columns )

categorical_data = classify_data(df)
analyzed_data = analyze_data(df)

def get_system_status(df,categorical_data,stats):

    at_risk_count = len(df[df['attendance']<50])
    top_performers = len(categorical_data['Top_performers'])
    std_dev = stats[1]

    if at_risk_count > 3 :
        return "CRITICAL ATTENTION REQUIRED"
    elif std_dev < 15 and top_performers >= 2:
        return "STABLE ACADAMIC SYSTEM"
    else:
        return "MODERATE PERFORMANCE"
status = get_system_status(df,categorical_data,analyzed_data['stats'])

print("Student data frame ")
print(df.to_string(index = False))

print("\n Student Categorisation : ")
for cat , ids in categorical_data.items():
    print(f"{cat} : {', '.join(map(str, ids))}")

print("\n Statistical Analysis :")
print(f"Mean Marks : {analyzed_data['stats'][0]:.2f}")
print(f"Standard Deviation : {analyzed_data['stats'][1]:.2f}")
print(f"Max Marks : {analyzed_data['stats'][2]:.2f}")
print(f"Correlation Coefficient (Marks vs Attendance) : {analyzed_data['correlation']:.2f}")

print(f"\n Academic System Status : {status}")



# Visualisation using seaborn and matplotlib  
plt.figure(figsize=(8,6))
sns.heatmap(df[['marks','attendance']].corr(),annot = True , cmap ='coolwarm', vmin=-1, vmax=1)












        

    

    