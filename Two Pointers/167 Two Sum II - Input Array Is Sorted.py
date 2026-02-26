# Two pointers on sorted array: narrow from both ends until pair sums to target
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(numbers) - 1

        while left <= right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # 1-indexed result
            elif total > target:
                right -= 1  # sum too big, shrink from right
            else:
                left += 1  # sum too small, grow from left

        return -1
