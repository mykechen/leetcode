# Set + sequence start detection: only count from numbers that are the start of a sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums)
        max_len = 0

        for n in num_set:
            if n - 1 not in num_set:  # n is the start of a sequence (no predecessor)
                length = 1

                while n + length in num_set:  # count consecutive numbers
                    length += 1

                max_len = max(max_len, length)

        return max_len