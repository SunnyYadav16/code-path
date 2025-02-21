"""
Problem 8: Pooh's To Do's
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and
print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...
"""

def print_todo_list(tasks):
    print("Pooh's To Dos:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i+1}. {task}")