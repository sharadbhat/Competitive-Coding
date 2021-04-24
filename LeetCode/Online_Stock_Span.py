# Leetcode
# https://leetcode.com/problems/online-stock-span


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days = 1
        while self.stack and self.stack[-1][0] <= price:
            _, prev = self.stack.pop()
            days += prev
        self.stack.append([price, days])
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
