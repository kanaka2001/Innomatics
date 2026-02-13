"""  5. Error Message Detector
Problem Statement:
Detect error messages from system logs.
logs = ["INFO", "ERROR", "WARNING", "ERROR"]
"""
logs = ["INFO", "ERROR", "WARNING", "ERROR"]
error_count = 0 
for log in logs:
    if log == "ERROR":
        print(f"Error detected: {log}")
        error_count += 1    
print(f"Total number of errors detected: {error_count}")