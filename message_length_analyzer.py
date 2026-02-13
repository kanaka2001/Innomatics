""" 4. Message Length Analyzer
Problem Statement:
Analyze message sizes.
messages = ["Hi", "Welcome to the platform", "OK"]
"""
messages = ["Hi", "Welcome to the platform", "OK"]
for message in messages:
    length = len(message)
    print(f"Message: '{message}' has length: {length}")
    if length > 10:
        print(f"This message '{message}' is longer than 10 characters so that we flaged it ")
