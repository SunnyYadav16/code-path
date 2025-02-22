"""
Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell
 out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g,
 e, and r removed from it.

Example Usage:
s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)

Example Output:
"suspcous"
""
"Hunny"

"""

def tiggerfy(s):
    return ''.join([char for char in s if char.lower() not in ['t', 'i', 'g', 'e', 'r']])