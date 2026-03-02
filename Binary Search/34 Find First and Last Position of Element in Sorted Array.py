class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def findStart(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    idx = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return idx

        def findEnd(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    idx = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return idx


        res = [-1, -1]
        res[0] = findStart(nums, target)
        res[1] = findEnd(nums, target)
        return res