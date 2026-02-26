# Fast-slow pointers: left tracks next non-zero position, right scans forward
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left = 0  # points to where next non-zero should go

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]  # swap non-zero to front
                left += 1
