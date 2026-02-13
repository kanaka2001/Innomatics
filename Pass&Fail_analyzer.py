""" 2. Pass / Fail Analyzer
Problem Statement:
Analyze student results.
marks = [45, 78, 90, 33, 60]
"""
marks = [45, 78, 90, 33, 66]
pass_count = 0
fail_count = 0

for mark in marks:
    if mark >=50:
        print("Pass")
        pass_count += 1
    else:
        print("Fail")
        fail_count += 1


pass_count= (f"Number of students passed : {pass_count}")
fail_count= (f"Number of students failed : {fail_count}")
print(pass_count)
print(fail_count)