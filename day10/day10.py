import pandas as pd
import numpy as np
import random
import math
import copy
def generate_student_data(n):
    data = []
    for i in range(n):
        record = {
            "id": 101 + i,
            "marks": random.randint(30, 95),
            "attendance": random.randint(40, 100),
            "scores": [random.randint(10, 20), random.randint(20, 30)] 
        }
        data.append(record)
    return data
def mutate_student_records(data_list, roll_mod):
    for i in range(len(data_list)):
        if i % roll_mod == 0:
            data_list[i]['marks'] = data_list[i]['marks'] + math.sqrt(data_list[i]['marks'])
            data_list[i]['scores'][0] += 10  
            data_list[i]['attendance'] = min(100, data_list[i]['attendance'] + 5)
    return data_list
def perform_drift_analysis(original_list, modified_list):
    orig_marks = [s['marks'] for s in original_list]
    mod_marks = [s['marks'] for s in modified_list]
    manual_mean_orig = sum(orig_marks) / len(orig_marks)
    mod_mean = np.mean(mod_marks)
    mod_std = np.std(mod_marks)
    drift = abs(manual_mean_orig - mod_mean)
    return {"manual_mean": manual_mean_orig, "mod_mean": mod_mean, "drift": drift, "std_dev": mod_std}

ROLL_NUMBER = 24110011667
MOD_VAL = ROLL_NUMBER % 3 if (667 % 3) != 0 else 1 # ensure we dont divide by zero
DRIFT_THRESHOLD = 7.0  + MOD_VAL# based on last digit of AP24110011667 and add MOD value to it to threshold 

original_data = generate_student_data(12)
shallow_copy_data = copy.copy(original_data)
deep_copy_data = copy.deepcopy(original_data)
mutate_student_records(shallow_copy_data, MOD_VAL)
analysis = perform_drift_analysis(deep_copy_data, shallow_copy_data)
copy_failure = False
if original_data[0]['scores'][0] != deep_copy_data[0]['scores'][0]:
    copy_failure = True
if copy_failure:
    final_status = "Copy Failure Detected"
elif analysis['drift'] > DRIFT_THRESHOLD:
    final_status = "Critical Drift"
elif analysis['drift'] > 2.0:
    final_status = "Minor Drift"
else:
    final_status = "Stable Data"
    
print("1. original Student DataFrame ")
print(pd.DataFrame(deep_copy_data).head())
print("\n2. shallow copy results  (first record scores)")
print(f"ID {shallow_copy_data[0]['id']} | mutated Scores: {shallow_copy_data[0]['scores']}")
print("\n3. deep copy results  (first record scores)")
print(f"ID {deep_copy_data[0]['id']} | original Scores: {deep_copy_data[0]['scores']}")
print(f"\n4.drift analysis: {analysis['drift']:.4f}")
print("\n5. statistical summary (tuple)")
stats_tuple = (round(analysis['manual_mean'], 2), round(analysis['drift'], 2), round(analysis['std_dev'], 2))
print(stats_tuple)
print(f"\n6. FINAL CLASSIFICATION: {final_status}")