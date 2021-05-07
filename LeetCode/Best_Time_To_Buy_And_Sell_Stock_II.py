# LeetCode
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sorted_prices = sorted(prices)
        if prices[::-1] == sorted_prices:
            return 0
        if prices == sorted_prices:
            return (prices[-1] - prices[0])
        profit = 0
        curr = 0
        start_curr = 0
        l = len(prices) - 1
        while curr < l:
            while curr < l and prices[curr] < prices[curr + 1]:
                curr += 1
            profit += (prices[curr] - prices[start_curr])
            while curr < l and prices[curr] >= prices[curr + 1]:
                curr += 1
            start_curr = curr
        return profit
