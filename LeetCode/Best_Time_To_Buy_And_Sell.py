# LeetCode
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        lowest = prices[0]
        max_profit = 0

        for i in prices:
            if max_profit < (i - lowest):
                max_profit = (i - lowest)
            if i < lowest:
                lowest = i
        return max_profit
