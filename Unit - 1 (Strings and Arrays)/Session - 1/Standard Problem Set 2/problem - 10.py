"""
Problem 10: Up and Down
Write a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the
number of odd numbers minus the number of even numbers in the list.

Example Usage:
lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)

Example Output:
1
3
-4
"""

def up_and_down(items):
    odd_count, even_count = 0, 0

    for i in items:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count - even_count
