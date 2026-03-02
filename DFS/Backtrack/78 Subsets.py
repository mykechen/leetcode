class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []

        def backtrack(path, idx):
            if idx == len(nums):
                res.append(path[:])
                return

            # get num
            path.append(nums[idx])
            backtrack(path, idx+1)
            path.pop()

            # skip num
            backtrack(path, idx+1)

        backtrack([], 0)
        return res