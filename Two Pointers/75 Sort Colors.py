class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # SOL 1: O(n) space complexity bc dict
        # freq = defaultdict(int)

        # for num in nums:
        #     freq[num] += 1

        # for i in range(len(nums)):
        #     if freq[0] > 0:
        #         nums[i] = 0
        #         freq[0] -= 1
        #     elif freq[1] > 0:
        #         nums[i] = 1
        #         freq[1] -= 1
        #     else:
        #         nums[i] = 2
        #         freq[2] -= 1

        # SOL 2: constant space complexity
        red = 0
        blue = len(nums) - 1
        white = 0

        while white <= blue:
            # if blue, swap
            if nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            # if red, swap
            elif nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            
