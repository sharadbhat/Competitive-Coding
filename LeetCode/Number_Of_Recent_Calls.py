# LeetCode
# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.q = []
        self.curr = 0
        self.length = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        self.length += 1
        while self.q[self.curr] < t - 3000 and self.length > 1:
            self.curr += 1
            self.length -= 1
        return self.length

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
