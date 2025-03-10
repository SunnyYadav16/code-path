"""
Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends.
Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even
groups. split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of
quantity.

Example Usage:
quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)

Example Output:
[1, 2, 3, 6]
[1]
"""

def split_haycorns(quantity):
    divisors = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            divisors.append(i)
    return divisors