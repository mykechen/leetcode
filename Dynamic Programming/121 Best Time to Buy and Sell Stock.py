class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy_p = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_p > p:
                buy_p = p

            profit = max(profit, p - buy_p)

        return profit
