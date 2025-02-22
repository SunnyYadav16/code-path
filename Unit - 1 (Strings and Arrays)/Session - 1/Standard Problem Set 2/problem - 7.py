"""
Problem 7: NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is
repeated x times. Do not use the * operator.

Example Usage
x = 6
nanana_batman(x)

x = 0
nanana_batman(x)

Example Output:
"nananananana batman!"
"batman!"
"""

def nanana_batman(x):
    new_string = ""
    for i in range(x):
        new_string += "na"

    return new_string + " batman!"
