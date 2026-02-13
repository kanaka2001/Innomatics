"""3. Simple Data Cleaner
Problem Statement:
Clean and standardize user names.
names = [" Alice ", "bob", " CHARLIE "]
"""
names = [" Alice ", "bob", " CHARLIE "]
print(f"Original names: {names}")

clean_list = [x.strip() for x in names]
print(f"Cleaned names: {clean_list}")