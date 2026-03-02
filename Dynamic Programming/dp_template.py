"""
=============================================================
DYNAMIC PROGRAMMING TEMPLATES
=============================================================
"""


# =============================================================
# 1. FIBONACCI / CLIMBING STAIRS PATTERN
# Use: current state depends on previous 1-2 states
# Examples: Climbing Stairs, House Robber, Fibonacci, Min Cost Stairs
# =============================================================

# Top-down (memoization)
def climb_stairs_memo(n):
    memo = {}

    def dp(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]

        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)


# Bottom-up (tabulation)
def climb_stairs_tab(n):
    if n <= 1:
        return 1

    prev2, prev1 = 1, 1

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


# =============================================================
# 2. HOUSE ROBBER PATTERN (TAKE OR SKIP)
# Use: pick elements with constraints (can't pick adjacent)
# Examples: House Robber, House Robber II, Delete and Earn
# =============================================================
def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, 0

    for num in nums:
        curr = max(prev1, prev2 + num)  # skip or take
        prev2 = prev1
        prev1 = curr

    return prev1


# =============================================================
# 3. 0/1 KNAPSACK PATTERN
# Use: pick items with weight/cost constraint, each item used once
# Examples: 0/1 Knapsack, Partition Equal Subset Sum, Target Sum
# =============================================================
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # skip item

            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])  # take item

    return dp[n][capacity]


# Space optimized (1D array)
def knapsack_01_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # reverse to avoid reuse
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


# =============================================================
# 4. UNBOUNDED KNAPSACK (ITEMS CAN BE REUSED)
# Use: pick items with no limit on reuse
# Examples: Coin Change, Coin Change II, Rod Cutting
# =============================================================
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Coin Change II (count combinations)
def coin_change_2(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:            # loop coins first to avoid counting permutations
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


# =============================================================
# 5. LONGEST COMMON SUBSEQUENCE (LCS) PATTERN
# Use: compare two sequences
# Examples: LCS, Edit Distance, Min Deletions to Make Equal
# =============================================================
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # match: take diagonal + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # skip one char

    return dp[m][n]


# =============================================================
# 6. EDIT DISTANCE PATTERN
# Use: transform one string to another with operations
# Examples: Edit Distance, Delete Operation for Two Strings
# =============================================================
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # base cases: empty string to non-empty
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # chars match, no operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete
                    dp[i][j - 1],      # insert
                    dp[i - 1][j - 1]   # replace
                )

    return dp[m][n]


# =============================================================
# 7. LONGEST INCREASING SUBSEQUENCE (LIS)
# Use: find longest increasing/decreasing subsequence
# Examples: LIS, Russian Doll Envelopes, Max Chain Length
# =============================================================

# O(n^2) approach
def lis(nums):
    n = len(nums)
    dp = [1] * n  # each element is a subsequence of length 1

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# O(n log n) approach with binary search
import bisect

def lis_optimized(nums):
    tails = []

    for num in nums:
        pos = bisect.bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)     # extend longest subsequence
        else:
            tails[pos] = num      # replace to keep smallest tail

    return len(tails)


# =============================================================
# 8. PALINDROME PATTERN
# Use: find palindromic substrings or subsequences
# Examples: Longest Palindromic Substring, Palindrome Partitioning
# =============================================================

# Longest Palindromic Substring (expand from center)
def longest_palindrome(s):
    res = ""

    def expand(left, right):
        nonlocal res
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(res):
                res = s[left:right + 1]
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)      # odd length
        expand(i, i + 1)  # even length

    return res


# Longest Palindromic Subsequence (DP)
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1  # single char is palindrome

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# =============================================================
# 9. GRID PATHS PATTERN
# Use: count paths or find min/max cost in a grid
# Examples: Unique Paths, Min Path Sum, Dungeon Game
# =============================================================
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # fill first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # fill rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]


# =============================================================
# 10. WORD BREAK PATTERN
# Use: can a string be segmented using a dictionary
# Examples: Word Break, Word Break II
# =============================================================
def word_break(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# =============================================================
# 11. STOCK BUYING/SELLING PATTERN
# Use: maximize profit with constraints on transactions
# Examples: Best Time to Buy/Sell Stock I, II, III, IV, with Cooldown
# =============================================================

# One transaction
def max_profit_one(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


# Unlimited transactions
def max_profit_unlimited(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


# With cooldown
def max_profit_cooldown(prices):
    if len(prices) < 2:
        return 0

    hold = -prices[0]     # holding a stock
    sold = 0              # just sold
    rest = 0              # cooldown / doing nothing

    for i in range(1, len(prices)):
        prev_hold = hold
        prev_sold = sold
        prev_rest = rest

        hold = max(prev_hold, prev_rest - prices[i])   # keep holding or buy
        sold = prev_hold + prices[i]                     # sell today
        rest = max(prev_rest, prev_sold)                 # rest or after cooldown

    return max(sold, rest)


# =============================================================
# 12. INTERVAL SCHEDULING / DECISION MAKING
# Use: make optimal decisions at each step
# Examples: Jump Game, Decode Ways, Paint House
# =============================================================
def can_jump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True


def decode_ways(s):
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        # single digit
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]

        # two digits
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# =============================================================
# CHEAT SHEET
# =============================================================
# Depends on prev 1-2 states        → 1. Fibonacci / Climbing stairs
# Take or skip with constraint       → 2. House robber
# Pick items, each used once         → 3. 0/1 Knapsack
# Pick items, unlimited reuse        → 4. Unbounded knapsack / Coin change
# Compare two sequences              → 5. LCS
# Transform one string to another    → 6. Edit distance
# Longest increasing/decreasing      → 7. LIS
# Palindrome questions               → 8. Expand from center / 2D DP
# Count paths / min cost in grid     → 9. Grid paths
# String segmentation                → 10. Word break
# Buy/sell stock problems            → 11. Stock pattern
# Optimal decisions at each step     → 12. Jump game / Decode ways