class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # SOL1: Dp slow
        # dp = [0] * len(prices)

        # for i in range(len(prices) - 2, -1, -1):
        #     dp[i] = max(0, prices[i+1] - prices[i]) + dp[i+1]

        # return dp[0]

        # Sol 2
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]

        return maxProfit