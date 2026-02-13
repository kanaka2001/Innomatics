""" 1. User Login Check
Problem Statement:
Given a username and password, check whether login is successful.
username = "admin"
password = "1234"
"""
print("Enter the username :")
username_input = input()
print("Enter the password :")
password_input = input()
if username_input == "admin" and password_input == "1234":
    print("Login successful.")
else:
    print("invalid credentials.")