"""
=============================================================
TWO POINTER TEMPLATES
=============================================================
"""


# =============================================================
# 1. OPPOSITE ENDS
# Use: sorted array, find pair/triplet, container problems
# Examples: Two Sum II, Container With Most Water, Valid Palindrome
# =============================================================
def two_pointer_opposite(nums, target):
    nums.sort()  # if needed
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]  # found answer
        elif total < target:
            left += 1             # need bigger
        else:
            right -= 1            # need smaller

    return []  # no answer found


# =============================================================
# 2. SAME DIRECTION (FAST-SLOW)
# Use: remove/modify in place, linked list cycle
# Examples: Remove Duplicates, Move Zeroes, Linked List Cycle
# =============================================================
def two_pointer_same_direction(nums):
    slow = 0

    for fast in range(len(nums)):
        if some_condition(nums[fast]):
            nums[slow] = nums[fast]
            slow += 1

    return slow


# =============================================================
# 3. THREE SUM (FIX ONE + TWO POINTER)
# Use: find triplets that meet a condition
# Examples: 3Sum, 3Sum Closest, 3Sum Smaller
# =============================================================
def three_sum(nums):
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        # skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                # skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1    # need bigger
            else:
                right -= 1   # need smaller

    return res


# =============================================================
# CHEAT SHEET
# =============================================================
# Sorted array + find pair → 1. Opposite ends
# Remove/modify in place   → 2. Fast-slow
# Find triplet             → 3. Fix one + opposite ends