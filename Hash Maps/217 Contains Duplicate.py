# Set: track seen numbers, return True as soon as a duplicate is found
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        unique = set()

        for n in nums:
            if n not in unique:
                unique.add(n)
            else:
                return True  # already seen this number

        return False