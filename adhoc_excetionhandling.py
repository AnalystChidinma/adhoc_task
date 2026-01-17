
"""
This script checks the elements in the list.
If any string value is detected, the script stops execution.
and send out the error message "string related data found,excution stopped! "

"""

data = [10, 50, "samuel", 2.5, "republic", 30, "simple"]

for item in data:
    if type(item) == str:
        raise Exception("string related data found, execution stopped!")
    print(item)
    
