class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # use binary search.
        # everytime that mid is odd, we decrement by 1 bc single element can't be on odd idx
        # check nums[mid] != nums[mid+1]: right = mid
        # if ==, we can just move left = mid + 2

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if mid % 2 == 1: # if mid is odd, decrement by 1 to make it even bc single element can't be on odd idx
                mid -= 1
            if nums[mid] != nums[mid+1]:
                right = mid # if mid and mid + 1 are not the same, then single element must be on the left side, so we move right to mid, and right could be mid
            else:
                left = mid + 2 # move + 2 bc we know mid and mid + 1 are the same, so we can skip both of them

        return nums[left]