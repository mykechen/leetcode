class Solution(object):
    def threeSumClosest(self, nums, target):
        # sort so we can use two pointer approach
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # update closest if current sum is nearer to target
                if abs(total - target) < abs(closest - target):
                    closest = total

                # move pointers based on comparison with target
                if total < target:
                    left += 1      # need a bigger sum
                elif total > target:
                    right -= 1     # need a smaller sum
                else:
                    return total   # exact match, can't do better

        return closest