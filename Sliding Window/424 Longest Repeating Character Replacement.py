class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        left = 0
        max_len = 0
        counts = defaultdict(int)

        for right in range(len(s)):
            counts[s[right]] += 1
            maxCounts = max(counts.values())
            curLen = right - left + 1

            if curLen - maxCounts > k: # dynamic window updates -> if curLen > k have to update
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len