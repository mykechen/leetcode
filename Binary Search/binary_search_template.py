"""
=============================================================
BINARY SEARCH TEMPLATES
=============================================================
"""


# =============================================================
# 1. BASIC BINARY SEARCH — FIND EXACT TARGET
# Use: find a specific value in sorted array
# Examples: Binary Search, Search Insert Position
# =============================================================
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # avoid overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found


# =============================================================
# 2. FIND LEFT BOUNDARY (FIRST OCCURRENCE)
# Use: find first position where condition is true
# Examples: First Bad Version, First Occurrence, Search Range (left)
# =============================================================
def find_left_boundary(nums, target):
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid     # save it, but keep searching left
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# =============================================================
# 3. FIND RIGHT BOUNDARY (LAST OCCURRENCE)
# Use: find last position where condition is true
# Examples: Search Range (right), Last Occurrence
# =============================================================
def find_right_boundary(nums, target):
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid     # save it, but keep searching right
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# =============================================================
# 4. SEARCH INSERT POSITION / BISECT LEFT
# Use: find where to insert target to keep array sorted
# Examples: Search Insert Position, Counting Smaller Numbers
# =============================================================
def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # left is the insertion point


# =============================================================
# 5. BINARY SEARCH ON ANSWER (MIN VALUE THAT SATISFIES)
# Use: search over answer space, not an array
# Examples: Koko Eating Bananas, Capacity to Ship Packages,
#           Split Array Largest Sum, Minimum Days to Make Bouquets
# =============================================================
def binary_search_on_answer_min(lo, hi):
    def is_feasible(value):
        # return True if this value satisfies the condition
        pass

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if is_feasible(mid):
            hi = mid         # mid works, try smaller
        else:
            lo = mid + 1     # mid doesn't work, try bigger

    return lo  # smallest value that satisfies


# =============================================================
# 6. BINARY SEARCH ON ANSWER (MAX VALUE THAT SATISFIES)
# Use: find maximum value where condition still holds
# Examples: Maximum Candies, Aggressive Cows
# =============================================================
def binary_search_on_answer_max(lo, hi):
    def is_feasible(value):
        # return True if this value satisfies the condition
        pass

    while lo < hi:
        mid = lo + (hi - lo + 1) // 2  # round UP to avoid infinite loop

        if is_feasible(mid):
            lo = mid         # mid works, try bigger
        else:
            hi = mid - 1     # mid doesn't work, try smaller

    return lo  # largest value that satisfies


# =============================================================
# 7. SEARCH IN ROTATED SORTED ARRAY
# Use: binary search when array is rotated
# Examples: Search in Rotated Sorted Array, Find Minimum
# =============================================================
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # target in left half
            else:
                left = mid + 1   # target in right half
        # right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # target in right half
            else:
                right = mid - 1  # target in left half

    return -1


# =============================================================
# 8. FIND MINIMUM IN ROTATED SORTED ARRAY
# Use: find pivot point in rotated array
# Examples: Find Minimum in Rotated Sorted Array
# =============================================================
def find_min_rotated(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1   # min is in right half
        else:
            right = mid      # min could be mid itself

    return nums[left]


# =============================================================
# 9. FIND PEAK ELEMENT
# Use: find local maximum
# Examples: Find Peak Element, Peak Index in Mountain Array
# =============================================================
def find_peak(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1   # peak is to the right
        else:
            right = mid      # peak could be mid itself

    return left


# =============================================================
# 10. BINARY SEARCH ON 2D MATRIX
# Use: search in row-sorted and column-sorted matrix
# Examples: Search a 2D Matrix, Search a 2D Matrix II
# =============================================================

# 2D Matrix (each row starts after previous row ends)
def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        # convert 1D index to 2D
        val = matrix[mid // cols][mid % cols]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# =============================================================
# CHEAT SHEET
# =============================================================
# Find exact value               → 1. Basic binary search
# Find first occurrence           → 2. Left boundary
# Find last occurrence            → 3. Right boundary
# Find insertion point            → 4. Search insert / bisect left
# Min value that works            → 5. Binary search on answer (min)
# Max value that works            → 6. Binary search on answer (max)
# Sorted but rotated array        → 7. Search rotated
# Find min in rotated             → 8. Find min rotated
# Find peak / local max           → 9. Find peak
# Search in 2D matrix             → 10. Binary search on matrix