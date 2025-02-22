"""
Problem 4: Non-decreasing Array
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing
by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example Usage:
nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)

Example Output:
True
False
"""


def non_decreasing(nums):
    violations = 0

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            violations += 1

            # If we already found more than one violation, returning False
            if violations > 1:
                print(violations)
                return False

            # fix the violation by modifying one of the elements
            if i > 0:
                # If we can't decrease nums[i] because of previous element,
                # we must increase nums[i+1]
                if nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
            # If it's the first element, we can always decrease it
            else:
                nums[i] = nums[i + 1]

    return True
