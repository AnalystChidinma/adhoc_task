"""
This script iterates through a list of elements.
It gracefully bypasses any string data and only processes non-string values.
without sending out any errors
-- it is the same as running data quality check in your data.
"""

data = [10, 50, "samuel", 2.5, "republic", 30, "simple"]

for item in data:
    if type(item) == str:
        continue     
    else:
        print(item)