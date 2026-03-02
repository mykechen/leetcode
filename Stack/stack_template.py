"""
=============================================================
STACK TEMPLATES
=============================================================
"""


# =============================================================
# 1. VALID PARENTHESES / BRACKET MATCHING
# Use: check if brackets are properly opened and closed
# Examples: Valid Parentheses, Remove Invalid Parentheses
# =============================================================
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in mapping:
            # closing bracket: check if it matches top of stack
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            # opening bracket: push to stack
            stack.append(ch)

    return len(stack) == 0


# =============================================================
# 2. MONOTONIC STACK — NEXT GREATER ELEMENT
# Use: find next greater/smaller element for each position
# Examples: Next Greater Element, Daily Temperatures,
#           Stock Span, Largest Rectangle in Histogram
# =============================================================

# Next GREATER element (decreasing stack)
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        # pop everything smaller than current
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result


# Next SMALLER element (increasing stack)
def next_smaller(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        # pop everything greater than current
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result


# =============================================================
# 3. DAILY TEMPERATURES (CLASSIC MONOTONIC STACK)
# Use: find how many days until warmer temperature
# Examples: Daily Temperatures
# =============================================================
def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []  # stores indices of temps waiting for warmer day

    for i in range(n):
        while stack and temps[stack[-1]] < temps[i]:
            idx = stack.pop()
            result[idx] = i - idx  # distance to warmer day

        stack.append(i)

    return result


# =============================================================
# 4. EVALUATE EXPRESSION / CALCULATOR
# Use: evaluate math expressions with operators
# Examples: Basic Calculator, Evaluate RPN
# =============================================================

# Evaluate Reverse Polish Notation
def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(float(a) / b))  # truncate toward zero
        else:
            stack.append(int(token))

    return stack[0]


# Basic Calculator (handles +, -, parentheses)
def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in "+-":
            result += sign * num
            num = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * num
            num = 0
            result *= stack.pop()  # sign before parenthesis
            result += stack.pop()  # result before parenthesis

    return result + sign * num


# =============================================================
# 5. MIN STACK (TRACK MINIMUM IN O(1))
# Use: stack that also returns minimum in constant time
# Examples: Min Stack
# =============================================================
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # tracks minimum at each level

    def push(self, val):
        self.stack.append(val)
        # push min of current val and current minimum
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# =============================================================
# 6. LARGEST RECTANGLE IN HISTOGRAM
# Use: find largest rectangle using monotonic stack
# Examples: Largest Rectangle in Histogram, Maximal Rectangle
# =============================================================
def largest_rectangle(heights):
    stack = []  # stores indices, maintains increasing heights
    max_area = 0
    heights.append(0)  # sentinel to flush remaining bars

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        stack.append(i)

    heights.pop()  # remove sentinel
    return max_area


# =============================================================
# 7. DECODE STRING
# Use: nested patterns with stack
# Examples: Decode String, Number of Atoms
# =============================================================
def decode_string(s):
    stack = []
    curr_str = ""
    curr_num = 0

    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == "[":
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif ch == "]":
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += ch

    return curr_str


# =============================================================
# 8. REMOVE DUPLICATES / SIMPLIFY WITH STACK
# Use: process string/array by removing based on neighbors
# Examples: Remove All Adjacent Duplicates, Simplify Path,
#           Remove K Digits
# =============================================================
def remove_adjacent_duplicates(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()  # remove pair
        else:
            stack.append(ch)

    return "".join(stack)


# =============================================================
# CHEAT SHEET
# =============================================================
# Matching brackets             → 1. Valid parentheses
# Next greater/smaller element  → 2. Monotonic stack
# Days until warmer             → 3. Daily temperatures
# Evaluate math expressions     → 4. Calculator / RPN
# Track min in O(1)             → 5. Min stack
# Largest rectangle             → 6. Histogram pattern
# Nested encoding/decoding      → 7. Decode string
# Remove based on neighbors     → 8. Remove duplicates