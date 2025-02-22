"""
Problem 3: T-I-Double Guh-Er II
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new
string that removes any substrings t, i, gg, and er from word. The function should be case-insensitive.

Example Usage:
word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
Example Output:

"r"
"eplan"
"chor"
"""

def tiggerfy(word):

    result = word.lower()

    patterns = ['gg', 'er', 't', 'i']
    for pattern in patterns:
        result = result.replace(pattern, "")

    return result

print(tiggerfy("Choir"))