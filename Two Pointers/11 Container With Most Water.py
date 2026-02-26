# Two pointers from opposite ends: move the shorter side inward to try to find more water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_water = 0

        while left <= right:
            cur_water = min(height[left], height[right]) * (right - left)  # area = min height * width
            max_water = max(max_water, cur_water)

            if height[left] < height[right]:
                left += 1  # move shorter side inward
            else:
                right -= 1

        return max_water
