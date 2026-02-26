# Dynamic sliding window: longest substring where (window size - most frequent char) <= k replacements
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        left = 0
        max_len = 0
        counts = defaultdict(int)  # frequency of each char in current window

        for right in range(len(s)):
            counts[s[right]] += 1
            maxCounts = max(counts.values())  # count of most frequent char in window
            curLen = right - left + 1

            # if replacements needed > k, shrink window from left
            if curLen - maxCounts > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len