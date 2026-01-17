"""
This code writes a Script that checks the data type of elements in a List, also  
filtered out the ones with string and has Republic at the beginning and Nigeria at the end.

"""

List = ["8", 
        8, 
        "Republic of Ireland", 
        "Federal Republic of Nigeria", 
        "Federal Republic of Germany", 
        "Federal Republic of Somalia"]


for num in List:
    if type(num) == str:
        if num.startswith("Republic") and num.endswith("Nigeria"):
            pass 
else:
    print("the dataset does not imply to any of the conditions")