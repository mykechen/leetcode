# Hash map: store complement (target - num) as key, check if current num was a previous complement
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Brute force O(n^2) — check every pair
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]
        # return -1

        # Optimized O(n) — hash map lookup for complement
        hash_map = {}  # maps complement -> index

        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in hash_map:  # current num is a complement we stored earlier
                return [hash_map[nums[i]], i]

            hash_map[diff] = i  # store complement for future lookup

        return -1