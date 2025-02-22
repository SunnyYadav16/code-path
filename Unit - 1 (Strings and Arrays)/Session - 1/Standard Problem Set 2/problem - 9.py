"""
Problem 9: Odd
Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers
in nums.

Example Usage
nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)

Example Output:
[1, 3]
[]
"""

def get_odds(items):
    new_list = []
    
    for i in items:
        if i % 2 != 0:
            new_list.append(i)

    return new_list