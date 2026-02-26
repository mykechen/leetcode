# Dutch National Flag: 3 pointers partition array into red(0), white(1), blue(2)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # SOL 1: O(n) space — count frequencies then overwrite
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

        # SOL 2: Dutch National Flag — O(1) space, single pass
        red = 0  # boundary for 0s (red)
        blue = len(nums) - 1  # boundary for 2s (blue)
        white = 0  # current element being examined

        while white <= blue:
            if nums[white] == 2:  # blue — swap to end
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            elif nums[white] == 0:  # red — swap to front
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:  # white — already in place
                white += 1
            
