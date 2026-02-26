# Sliding window + set: expand right, shrink left when duplicate found
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        k = 0
        left = 0
        charSet = set()  # tracks chars in current window

        for right in range(len(s)):
            while s[right] in charSet:  # shrink until no duplicate
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            k = max(k, right-left+1)  # update max length

        return k