# Sort + fix one number + two pointers: find all unique triplets summing to 0
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()  # sort to enable two pointer approach and skip duplicates

        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicate first element
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # need bigger sum
                elif total > 0:
                    right -= 1  # need smaller sum
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left-1] and left < right:  # skip duplicate second element
                        left += 1

        return res