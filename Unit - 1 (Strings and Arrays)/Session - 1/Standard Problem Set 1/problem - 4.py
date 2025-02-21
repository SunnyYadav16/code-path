"""
Problem 4: Return Item
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the
element at index x in items. If x is not a valid index of items, return None.
"""

def get_item(items, x):
    if x < 0 or x >= len(items):
        return None
    else:
        return items[x]