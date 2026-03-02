class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        low, high = 1, max(piles)

        while low <= high:
            k = (low + high) // 2
            
            # getting the number of hours at current k
            if sum((pile + k - 1) // k for pile in piles) > h:
                low = k + 1
            else:
                high = k - 1
            
        return low
