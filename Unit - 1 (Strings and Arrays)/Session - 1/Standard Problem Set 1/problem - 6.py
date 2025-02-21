"""
Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a
parameter and multiplies each element in the list by two. Return the doubled list.
"""

def doubled(hunny_jars):
    return [jar * 2 for jar in hunny_jars]