# Prefix sum + hash map: if prefix[j] - prefix[i] == k, subarray [i+1..j] sums to k
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        prefix = 0
        seen = defaultdict(int)  # prefix sum -> number of times seen
        seen[0] = 1  # base case: empty prefix

        for num in nums:
            prefix += num
            if prefix - k in seen:  # a previous prefix exists such that the difference is k
                count += seen[prefix - k]
            seen[prefix] += 1

        return count