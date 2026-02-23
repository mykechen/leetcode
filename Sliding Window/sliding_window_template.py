"""
=============================================================
SLIDING WINDOW TEMPLATES
=============================================================
"""


# =============================================================
# 1. DYNAMIC SIZE — LONGEST/MAX
# Use: find longest subarray/substring meeting a condition
# Examples: Longest Substring Without Repeating, Max Consecutive Ones
# =============================================================
def sliding_window_longest(nums, condition):
    left = 0
    max_length = 0

    for right in range(len(nums)):
        # expand: add nums[right] to window logic

        # shrink: while condition is violated
        while not condition():
            # remove nums[left] from window logic
            left += 1

        # update result
        max_length = max(max_length, right - left + 1)

    return max_length


# =============================================================
# 2. DYNAMIC SIZE — SHORTEST/MIN
# Use: find shortest subarray meeting a condition
# Examples: Minimum Size Subarray Sum, Minimum Window Substring
# =============================================================
def sliding_window_shortest(nums, condition):
    left = 0
    min_length = float('inf')

    for right in range(len(nums)):
        # expand: add nums[right] to window logic

        # shrink: while condition IS met, try to shrink
        while condition():
            min_length = min(min_length, right - left + 1)
            # remove nums[left] from window logic
            left += 1

    return min_length if min_length != float('inf') else 0


# =============================================================
# 3. FIXED SIZE
# Use: window of exact size k
# Examples: Find All Anagrams, Max Sum Subarray of Size K
# =============================================================
def sliding_window_fixed(nums, k):
    # build initial window
    window_sum = sum(nums[:k])
    best = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]       # add new right
        window_sum -= nums[i - k]   # remove old left
        best = max(best, window_sum)

    return best


# =============================================================
# CHEAT SHEET
# =============================================================
# Longest subarray with condition  → 1. Dynamic (longest)
# Shortest subarray with condition → 2. Dynamic (shortest)
# Window of exact size k           → 3. Fixed